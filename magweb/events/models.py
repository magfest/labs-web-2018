from datetime import datetime
import requests
import json

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


class EventPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True, null=True)
    media = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    template_name = models.CharField(max_length=254, null=True, blank=True, db_index=True)
    homepage_template_name = models.CharField(max_length=254, null=True, blank=True, db_index=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image'),
        DocumentChooserPanel('media'),
        FieldPanel('template_name'),
        FieldPanel('homepage_template_name'),
        InlinePanel('events', heading='Event Years')

    ]

    def get_template(self, request, *args, **kwargs):
        template = super(EventPage, self).get_template(request, *args, **kwargs)
        if self.template_name:
            template = '{slug}/{template}'.format(slug=self.template_name, template=template)
        return template

    def get_context(self, request, *args, **kwargs):
        context = super(EventPage, self).get_context(request, *args, **kwargs)
        context['event'] = self.events.order_by('start_date').first()
        context['title'] = str(context['event'])
        context['year'] = context['event'].year
        if context['event'].show_registration:
            context['registration_url'] = context['event'].registration_link
        if context['event'].show_hotels:
            context['hotel_url'] = context['event'].hotel_link
        context['guest_types'] = {}
        context['nav'] = self.get_children().live().in_menu()
        for page in self.get_children():
            if page.content_type.model == 'guestpage':
                context['guest_types'][page.title] = page.specific.guests.all()

        return context


class Event(Orderable, models.Model):
    event = ParentalKey(EventPage, on_delete=models.CASCADE, db_index=True, related_name='events')
    price = models.FloatField(db_index=True, blank=True, null=True, verbose_name='Current Price')
    show_registration = models.BooleanField(db_index=True, default=True)
    show_hotels = models.BooleanField(db_index=True, default=True)

    # Registration Info
    registration_link = models.URLField(
        help_text='Uber registration URL',
        null=True,
        blank=True
    )
    hotel_link = models.URLField(
        help_text='Hotel booking URL',
        null=True,
        blank=True
    )

    # Uber API Info
    api_url = models.URLField(
        verbose_name='API Url',
        help_text='Event Uber API url',
        blank=True
    )
    api_token = models.CharField(
        max_length=48,
        verbose_name='Uber API Token',
        blank=True
    )

    # Event info (determined by Uber API)
    event_name = models.CharField(max_length=64, verbose_name='Name', blank=True)
    org_name = models.CharField(max_length=64, blank=True, verbose_name='Organization Name')
    year = models.CharField(max_length=4, blank=True)
    epoch = models.DateTimeField(blank=True, null=True)
    eschaton = models.DateTimeField(blank=True, null=True)

    venue = models.CharField(max_length=128, verbose_name='Venue Name', blank=True)
    venue_address = models.CharField(max_length=128, verbose_name='Venue Address', blank=True)

    at_the_con = models.BooleanField(blank=True, default=False)
    post_con = models.BooleanField(blank=True, default=False)

    panels = [
        PageChooserPanel('event'),
        FieldPanel('event_name', heading='Name'),
        FieldPanel('venue', heading='Venue'),
        FieldPanel('venue_address', heading='Venue Address'),
        FieldPanel('epoch', heading='Event Opening'),
        FieldPanel('eschaton', heading='Event Closing'),
        FieldPanel('api_token', heading='UBER API Token'),
        FieldPanel('api_url', heading='UBER Root URL'),
        FieldPanel('price', heading='Current Badge Price',
                   help_text='This field will be automatically updated if possible.'),
        MultiFieldPanel([
            FieldPanel('registration_link', heading='Registration Link'),
            FieldPanel('show_registration', heading='Show link to register?'),
            FieldPanel('hotel_link', heading='Hotel Booking Link'),
            FieldPanel('show_hotels', heading='Show link to book hotels?')
        ], heading='Settings')
    ]

    @property
    def jsonrpc_api(self):
        return '{}/uber/jsonrpc/'.format(self.api_url)

    def save(self, *args, **kwargs):
        headers = {
            'content-type': 'application/json',
            'X-Auth-Token': self.api_token
        }
        payload = {
            "method": "config.info",
            "jsonrpc": "2.0",
        }
        response = None

        if self.api_url:
            self.api_url = self.api_url.strip('/')
            if not self.registration_link:
                self.registration_link = '{}/uber/preregistration/form/'.format(self.api_url)
            response = requests.post(
                self.jsonrpc_api, data=json.dumps(payload), headers=headers)\

            response = response.json()

        if response and response['result']:
            uber_config = response['result']

            self.api_version = uber_config['API_VERSION']
            self.event_name = uber_config['EVENT_NAME']
            self.org_name = uber_config['ORGANIZATION_NAME']
            if uber_config['YEAR']:
                self.year = uber_config['YEAR']
            else:
                self.year = datetime.strptime(uber_config['EPOCH'], '%Y-%m-%d %H:%M:%S.000000').year
            self.epoch = uber_config['EPOCH']
            self.eschaton = uber_config['ESCHATON']

            self.venue = uber_config['EVENT_VENUE']
            self.venue_address = uber_config['EVENT_VENUE_ADDRESS']

            self.at_the_con = uber_config['AT_THE_CON']
            self.post_con = uber_config['POST_CON']
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return '{event} {year}'.format(event=self.event_name, year=self.year)

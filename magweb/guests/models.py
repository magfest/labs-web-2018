from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.shortcuts import render, HttpResponse

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, BaseChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from magweb.events.models import Event
from magweb.utils import iterable_to_dict

User = get_user_model()


class GuestTag(TaggedItemBase):
    content_object = ParentalKey(
        'Guest',
        related_name='tag_set',
        on_delete=models.CASCADE
    )


@register_snippet
class Guest(index.Indexed, ClusterableModel):
    name = models.CharField(
        max_length=254
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image'),
        InlinePanel('years', heading='Events Attended'),
        InlinePanel('urls', heading='Social Media URLs')
    ]

    def __str__(self):
        return self.name

    def to_dict(self):
        dict_self = {
            'name': self.name,
            'image': self.image,
            'urls': self.url_dicts,
            'years': self.year_dicts,
        }
        return dict_self

    @property
    def year_dicts(self):
        return iterable_to_dict(self.years.all())

    @property
    def url_dicts(self):
        return iterable_to_dict(self.urls.all())

    @property
    def recent_year(self):
        year = self.years.order_by('event__epoch', 'event__event_name').first()
        items = {
            'urls': iterable_to_dict(self.urls.all())
        }
        items.update(year.to_dict())
        return items

    def year(self, year):
        year = self.years.filter(event__year__exact=year).first()
        if year:
            items = {
                'urls': iterable_to_dict(self.urls.all())
            }
            items.update(year.to_dict())
            return items


class GuestPage(RoutablePageMixin, Page):
    content_panels = Page.content_panels + [
        InlinePanel('guests', heading='Guests to Display')
        # ...
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(GuestPage, self).get_context(request, *args, **kwargs)
        return context

    @route('^(\d+)/$')
    def by_year(self, request, *args, **kwargs):
        return HttpResponse(content=render(request, self.template), status=200)


class GuestYear(Orderable, ClusterableModel):
    guest = ParentalKey(Guest, on_delete=models.CASCADE, related_name='years', db_index=True)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='+')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)

    panels = [
        FieldPanel('event'),
        MultiFieldPanel([
            FieldPanel('body')
        ]),
        ImageChooserPanel('image'),


    ]

    @property
    def name(self):
        return self.guest.name

    def to_dict(self):
        items = {
            'name': self.name,
            'image': self.image,
            'body': self.body,
        }
        return items

    def __str__(self):
        return '{} - {}'.format(self.guest.name, str(self.event))


class GuestPagePlacement(Orderable, models.Model):
    page = ParentalKey(GuestPage, on_delete=models.CASCADE, related_name='guests')
    guest = models.ForeignKey(GuestYear, on_delete=models.CASCADE, related_name='+')

    panels = [
        BaseChooserPanel('guest')
    ]

    def __str__(self):
        return self.page.title + "->" + self.guest.name

    def get_guest(self):
        return self.guest


class GuestURL(Orderable, models.Model):
    guest = ParentalKey(Guest, on_delete=models.CASCADE, related_name='urls', db_index=True)
    url = models.URLField(db_index=True)
    name = models.CharField(blank=True, null=True, db_index=True, max_length=254)

    panels = [
        FieldPanel('name'),
        FieldPanel('url')
    ]

    def __str__(self):
        return '{} - {}'.format(self.guest.name, self.name if self.name else self.url)

    def to_dict(self):
        return {
            self.name.lower(): self.url
        }

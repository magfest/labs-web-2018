import json
from datetime import datetime

import requests
from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import BaseStreamBlock

TYPE_CHOICE = (
    ('prod', 'Production'),
    ('dev', 'Development')
)

@register_setting
class EventSettings(BaseSetting):
    event_type = models.CharField(
        max_length=8,
        verbose_name='Event Type',
        choices=TYPE_CHOICE,
        blank=False
    )

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
        blank=False
    )
    api_token = models.CharField(
        max_length=48,
        verbose_name='Uber API Token',
        blank=False
    )

    # Event info (determined by Uber API)
    event_name = models.CharField(max_length=64, verbose_name='Name', blank=True)
    org_name = models.CharField(max_length=64, blank=True, verbose_name='Organization Name')
    year = models.CharField(max_length=4, blank=True)
    epoch = models.DateTimeField(blank=True, null=True)

    venue = models.CharField(max_length=128, verbose_name='Venue Name', blank=True)
    venue_address = models.CharField(max_length=128, verbose_name='Venue Address', blank=True)

    at_the_con = models.BooleanField(blank=True)
    post_con = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):
        headers = {
            'content-type': 'application/json',
            'X-Auth-Token': self.api_token
        }
        payload = {
            "method": "config.info",
            "jsonrpc": "2.0",
        }
        response = requests.post(
            self.api_url, data=json.dumps(payload), headers=headers).json()

        if response['result']:
            uber_config = response['result']

            self.api_version = uber_config['API_VERSION']
            self.event_name = uber_config['EVENT_NAME']
            self.org_name = uber_config['ORGANIZATION_NAME']
            if uber_config['YEAR']:
                self.year = uber_config['YEAR']
            else:
                self.year = datetime.strptime(uber_config['EPOCH'], '%Y-%m-%d %H:%M:%S.000000').year
            self.epoch = uber_config['EPOCH']

            self.venue = uber_config['EVENT_VENUE']
            self.venue_address = uber_config['EVENT_VENUE_ADDRESS']

            self.at_the_con = uber_config['AT_THE_CON']
            self.post_con = uber_config['POST_CON']
        super(EventSettings, self).save(*args, **kwargs)


class StandardPage(Page):

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body')
    ]
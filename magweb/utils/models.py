import json
from datetime import datetime

import requests
from django.db import models

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable

from .blocks import BaseStreamBlock


class StandardPage(Page):

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        InlinePanel('placement', heading='Events To Link This Page To')
    ]


class PagePlacement(Orderable, models.Model):
    page = ParentalKey(StandardPage, on_delete=models.CASCADE, db_index=True,
                       related_name='placement')
    parent = ParentalKey('events.EventPage', on_delete=models.CASCADE, db_index=True,
                         related_name='pages')

    panels = [
        FieldPanel('parent')
    ]

    def __str__(self):
        return self.parent.title + "->" + self.page.title

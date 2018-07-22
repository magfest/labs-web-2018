import json
import requests
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, BaseChooserPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from magweb.events.models import Event
from magweb.utils import iterable_to_dict

User = get_user_model()


class AnnouncementTag(TaggedItemBase):
    content_object = ParentalKey(
        'Announcement',
        related_name='tag_set',
        on_delete=models.CASCADE
    )


@register_snippet
class Announcement(index.Indexed, ClusterableModel):
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
    body = RichTextField()
    tags = ClusterTaggableManager(through=AnnouncementTag, blank=True)

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image'),
        FieldPanel('body'),
        FieldPanel('tags'),
        InlinePanel('events', heading='Events'),
        InlinePanel('authors', heading='Authors')
    ]

    def __str__(self):
        return self.name

    def to_dict(self):
        items = {
            'name': self.name,
            'image': self.image,
            'body': self.body,
            'authors': iterable_to_dict(self.authors)
        }
        return items


class AnnouncementPage(Page):

    content_panels = Page.content_panels + [
        # InlinePanel('announcements'),
        # ...
    ]


class AnnouncementEventPlacement(Orderable, models.Model):
    announcement = ParentalKey(Announcement, related_name='events', on_delete=models.CASCADE,
                               db_index=True)
    event = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )
    panels = [
        PageChooserPanel('event')
    ]


class AnnouncementAuthor(Orderable, models.Model):
    announcement = ParentalKey(Announcement, related_name='authors', on_delete=models.CASCADE,
                               db_index=True)
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('author')
    ]

    def to_dict(self):
        items = {
            'name': self.author.name,
        }
        return items

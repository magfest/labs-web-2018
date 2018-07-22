from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField, ParentalManyToManyDescriptor
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from magweb.events.models import EventPage


class HomePage(Page):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()

    events = ParentalManyToManyField(EventPage, related_name='homepages', db_index=True, blank=True)

    footer = models.ForeignKey(
        'home.Footer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('logo'),
        FieldPanel('body'),
        FieldPanel('events'),
        SnippetChooserPanel('footer')
    ]

    def __str__(self):
        return self.title

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['events'] = self.events.all()
        for event in context['events']:
            print(event)
        return context


@register_snippet
class Footer(index.Indexed, ClusterableModel):
    trademark = RichTextField(blank=True, null=True, db_index=True)
    slogan = RichTextField(blank=True, null=True, db_index=True)

    panels = [
        FieldPanel('trademark')
    ]

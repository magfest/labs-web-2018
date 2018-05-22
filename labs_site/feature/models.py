from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page, Collection

class FeaturePage(Page):
    description = models.TextField(
        help_text='Describe the feature'
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    gallery = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=['Root']),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Select the image collection for this gallery.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('gallery'),
    ]

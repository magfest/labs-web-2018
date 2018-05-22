from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    hero_headline = models.CharField(
        max_length=128,
        help_text='Event introduction headline'
    )
    hero_text = models.TextField(
        help_text='Event introduction paragraph'
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_headline', classname="full"),
        FieldPanel('hero_text', classname="full")
    ]

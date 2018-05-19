from django.db import models

# Create your models here.
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting
class EventSettings(BaseSetting):
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
import json
import requests
from datetime import datetime

from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel

@register_snippet
class Guest(index.Indexed, ClusterableModel):
    name = models.CharField(
        max_length=254
    )
    bio = RichTextField()
    picture = models.URLField()
    facebook_handle = models.URLField()
    twitter_handle = models.TextField(
        max_length=16
    )
    website = models.URLField()




    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-150x150').img_tag()
        except:
            return ''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'


@register_snippet
class Band(Guest):
    song_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Band'
        verbose_name_plural = 'Bands'



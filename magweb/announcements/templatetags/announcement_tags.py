from django import template
from ..models import Announcement

register = template.Library()


# Advert snippets
@register.inclusion_tag('announcements/tags/announcements.html', takes_context=True)
def announcements(context):
    return {
        'announcements': Announcement.objects.all(),
        'request': context['request'],
    }

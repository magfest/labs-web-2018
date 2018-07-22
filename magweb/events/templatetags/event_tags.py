from django import template
from ..models import Event

register = template.Library()


# Advert snippets
@register.inclusion_tag('events/tags/events.html', takes_context=True)
def events(context):
    return {
        'events': Event.objects.all(),
        'request': context['request'],
    }

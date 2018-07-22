from django import template
from ..models import Guest

register = template.Library()


# Advert snippets
@register.inclusion_tag('guests/tags/guests.html', takes_context=True)
def guests(context):
    return {
        'guests': Guest.objects.all(),
        'request': context['request'],
    }

from django import template

register = template.Library()

@register.filter
def truncate_to_300_words(value):
    words = value.split()
    if len(words) > 300:
        value = ' '.join(words[:300]) + '...'
    return value
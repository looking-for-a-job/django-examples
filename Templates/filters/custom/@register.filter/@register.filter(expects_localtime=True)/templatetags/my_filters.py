#!/usr/bin/env python
from django import template

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#filters-and-time-zones
"""

register = template.Library()

@register.filter
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ''

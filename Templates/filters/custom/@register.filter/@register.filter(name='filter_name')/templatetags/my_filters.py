#!/usr/bin/env python
from django import template

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#registering-custom-filters
"""

register = template.Library()

@register.filter(name='filter_name')
def my_filter(value):
    return "filter input: %s" % value

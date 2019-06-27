#!/usr/bin/env python
from django import template

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#registering-custom-filters
"""

register = template.Library()

@register.filter
def my_not_save_filter(value):
    return "filter input: %s" % value

@register.filter(is_safe=True)
def my_save_filter(value):
	return "filter input: %s" % value

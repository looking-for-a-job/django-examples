#!/usr/bin/env python
from django import template
from django.template.defaultfilters import stringfilter

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#django.template.defaultfilters.stringfilter
"""

register = template.Library()

@register.filter
@stringfilter
def my_filter(value):
	return "filter input: %s" % value.lower()

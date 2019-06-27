#!/usr/bin/env python
from django import template

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#simple-tags
"""

register = template.Library()

# @register.simple_tag(name='tag_name')

@register.simple_tag
def my_args_tag(arg1,arg2):
    return "my_args_tag: arg1 = %s, arg2 = %s" % (arg1,arg2)

@register.simple_tag(takes_context=True)
def my_context_tag(context):
    return "my_context_tag: arg1 = %s" % context["arg1"]




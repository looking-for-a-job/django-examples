#!/usr/bin/env python
from django import template

"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags
"""

register = template.Library()

@register.inclusion_tag('templatetags/my_args_tag.html', takes_context=False)
def my_args_tag(a, b, *args, **kwargs):
    return {'a': a, 'b': b, **kwargs}

@register.inclusion_tag('templatetags/my_context_tag.html', takes_context=True)
def my_context_tag(context):
    return context
    # return {'arg1': context['arg1'],'arg2': context['arg2']}

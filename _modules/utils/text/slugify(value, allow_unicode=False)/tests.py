#!/usr/bin/env python
from django.utils.text import slugify

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.text.slugify

slugify(value, allow_unicode=False)
"""

assert slugify(' Joel is a slug ')=='joel-is-a-slug'


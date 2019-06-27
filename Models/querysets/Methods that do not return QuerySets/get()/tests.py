#!/usr/bin/env python
from django.core.exceptions import ObjectDoesNotExist
from .models import Blog, Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#create

get(**kwargs)
"""

try:
    e = Entry.objects.get(id=42)
    b = Blog.objects.get(id=42)
except ObjectDoesNotExist:
    print("Either the entry or blog doesn't exist.")


try:
    e = Entry.objects.get(id=42)
except Entry.DoesNotExist:
    pass

#!/usr/bin/env python
from .models import Blog, Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#delete
"""

b = Blog.objects.get(pk=1)
Entry.objects.filter(blog=b).delete()

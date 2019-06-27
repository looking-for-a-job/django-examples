#!/usr/bin/env python
from .models import Blog, Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#explain

explain(format=None, **options)
"""

print(Blog.objects.filter(name='My Blog').explain())

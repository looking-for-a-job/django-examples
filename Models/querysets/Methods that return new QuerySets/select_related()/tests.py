#!/usr/bin/env python
from django.db import connection
from .models import Blog, Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-related

select_related(*fields)
"""

qs = Entry.objects.all()
print(qs.query)

qs = Entry.objects.select_related('blog')
print(qs.query)


#!/usr/bin/env python
from .models import Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#latest

latest(*fields)
"""

try:
    e = Entry.objects.latest('pub_date', '-expire_date')
except Entry.DoesNotExist:
    pass
"""
    class Meta:
        get_latest_by = ["pub_date"]
e = Entry.objects.latest()
"""

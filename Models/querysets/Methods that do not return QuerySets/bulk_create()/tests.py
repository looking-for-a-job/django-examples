#!/usr/bin/env python
from .models import Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#bulk-create

bulk_create(objs, batch_size=None, ignore_conflicts=False)
"""

Entry.objects.bulk_create([
    Entry(headline='This is a test'),
    Entry(headline='This is only a test'),
])

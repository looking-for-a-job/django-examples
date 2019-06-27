#!/usr/bin/env python
from .models import Entry

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#bulk-update

bulk_update(objs, fields, batch_size=None)
"""

objs = [
    Entry.objects.create(headline='Entry 1'),
    Entry.objects.create(headline='Entry 2'),
]
objs[0].headline = 'This is entry 1'
objs[1].headline = 'This is entry 2'
Entry.objects.bulk_update(objs, ['headline'])

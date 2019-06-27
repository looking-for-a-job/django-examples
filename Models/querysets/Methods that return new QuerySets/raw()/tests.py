#!/usr/bin/env python
from django.db import transaction
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#raw

raw(raw_query, params=None, translations=None)
"""

qs = MyModel.objects.raw('SELECT * FROM %s' % MyModel._meta.db_table)
for r in qs:
    print(r)

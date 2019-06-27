#!/usr/bin/env python
import django
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#distinct

distinct(*fields)
"""

qs = MyModel.objects
qs = q.distinct('title')
try:
    for r in qs.all():
        print(r.title)
# django.db.utils.NotSupportedError: DISTINCT ON fields is not supported by this database backend
except django.db.utils.NotSupportedError:
    print("not supported")
    qs = MyModel.objects.values_list('title', flat=True).distinct()
    for r in qs.all():
        print(r.title)

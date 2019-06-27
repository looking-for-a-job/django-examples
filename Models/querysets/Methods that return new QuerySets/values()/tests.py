#!/usr/bin/env python
import django
from django.db.models.functions import Lower
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#values

values(*fields, **expressions)
"""

qs = MyModel.objects.values()
for data in qs:
    print(data["title"])

qs = MyModel.objects.values(lower_title=Lower('title'))
for data in qs:
    print(data["lower_title"])

#!/usr/bin/env python
from django.db.models import Value
from django.db.models.functions import LPad
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#lpad

class LPad(expression, length, fill_text=Value(' '), **extra)
"""

qs = MyModel.objects.annotate(lpad=LPad('name', 8, Value('-')))
for r in qs.all():
    print(r.lpad)

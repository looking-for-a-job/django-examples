#!/usr/bin/env python
from django.db.models import Value
from django.db.models.functions import Replace
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#replace

class Replace(expression, text, replacement=Value(''), **extra)
"""

qs = MyModel.objects.annotate(new_name=Replace('name', Value(' '), Value('-')))
for r in qs.all():
    print(r.new_name)

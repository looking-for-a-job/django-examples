#!/usr/bin/env python
from django.db.models import Count
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/expressions/#django.db.models.Expression.asc

asc(nulls_first=False, nulls_last=False)
"""

qs = MyModel.objects.order_by('?') # order randomly
print(qs.all())

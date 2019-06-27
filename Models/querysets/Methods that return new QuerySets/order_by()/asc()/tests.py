#!/usr/bin/env python
from django.db.models import Count
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#annotate

asc(nulls_first=False, nulls_last=False)
"""

qs = MyModel.objects.order_by('title').asc()
print(qs.all())

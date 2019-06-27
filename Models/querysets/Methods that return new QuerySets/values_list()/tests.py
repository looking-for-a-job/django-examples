#!/usr/bin/env python
import django
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#values-list

values_list(*fields, flat=False, named=False)
"""

qs = MyModel.objects.values_list('id', 'title')
for t in qs.all():
    print(t[0],t[1]) # tuple

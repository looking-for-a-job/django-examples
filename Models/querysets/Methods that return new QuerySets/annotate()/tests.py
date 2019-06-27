#!/usr/bin/env python
from django.db.models import Count
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#annotate

annotate(*args, **kwargs)
"""

qs = MyModel.objects.annotate(column_name=Count('id'))
print(q[0].column_name)

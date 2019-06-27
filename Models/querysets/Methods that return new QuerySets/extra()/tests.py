#!/usr/bin/env python
from django.db import connection
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#extra

extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
"""

qs = MyModel.objects.all()
qs = qs.extra(select={'is_recent': "pub_date > '2006-01-01'"})
print(qs.query)


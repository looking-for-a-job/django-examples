#!/usr/bin/env python
from django.db.models.functions import RTrim
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#rtrim

class RTrim(expression, **extra)
"""

qs = MyModel.objects.annotate(value=RTrim('name'))
for r in qs.all():
    print(r.value)

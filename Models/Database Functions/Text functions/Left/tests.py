#!/usr/bin/env python
from django.db.models.functions import Left
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#left

class Left(expression, length, **extra)
"""

qs = MyModel.objects.annotate(first_initial=Left('name', 1))
for r in qs.all():
    print(r.first_initial)

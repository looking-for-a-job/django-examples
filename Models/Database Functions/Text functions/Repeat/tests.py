#!/usr/bin/env python
from django.db.models.functions import Repeat
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#repeat

class Repeat(expression, number, **extra)
"""

qs = MyModel.objects.annotate(name_3x=Repeat('name', 3))
for r in qs.all():
    print(r.name_3x)

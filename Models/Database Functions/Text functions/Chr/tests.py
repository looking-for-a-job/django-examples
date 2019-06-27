#!/usr/bin/env python
from django.db.models.functions import Chr
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#chr

class Chr(expression, **extra)
"""

qs = MyModel.objects.filter(name__startswith=Chr(ord('M')))
for r in qs.all():
    print(r.name)

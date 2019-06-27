#!/usr/bin/env python
from django.db.models.functions import Length
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#length

class Length(expression, **extra)
"""

qs = MyModel.objects.annotate(name_length=Length('name'))
for r in qs.all():
    print(r.name, r.name_length)

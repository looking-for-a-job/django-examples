#!/usr/bin/env python
from django.db.models.functions import Lower
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#lower

class Lower(expression, **extra)
"""

qs = MyModel.objects.annotate(name_lower=Lower('name'))
for r in qs.all():
    print(r.name,r.name_lower)

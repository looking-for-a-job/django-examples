#!/usr/bin/env python
from django.db.models.functions import Ord
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#ord

class Ord(expression, **extra)
"""

qs = MyModel.objects.annotate(name_code_point=Ord('name'))
for r in qs.all():
    print(r.name[0],r.name_code_point)

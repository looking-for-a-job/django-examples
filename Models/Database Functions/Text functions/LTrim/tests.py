#!/usr/bin/env python
from django.db.models.functions import LTrim
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#ltrim

class LTrim(expression, **extra)
"""

qs = MyModel.objects.annotate(value=LTrim('name'))
for r in qs.all():
    print(r.value)

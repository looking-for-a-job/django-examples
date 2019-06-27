#!/usr/bin/env python
from django.db.models import FloatField
from django.db.models.functions import Cast
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#cast

class Cast(expression, output_field)

Forces the result type of expression to be the one from output_field
"""

qs = MyModel.objects.annotate(as_float=Cast('integer', FloatField()))
for r in qs.all():
    print(r.as_float)

#!/usr/bin/env python
from django.db.models.functions import Reverse
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#reverse

class Reverse(expression, **extra)
"""

qs = MyModel.objects.annotate(backward=Reverse('name'))
for r in qs.all():
    print(r.backward)

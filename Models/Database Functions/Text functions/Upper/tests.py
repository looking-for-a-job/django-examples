#!/usr/bin/env python
from django.db.models.functions import Upper
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#upper

class Upper(expression, **extra)
"""

qs = MyModel.objects.annotate(name_upper=Upper('name'))
for r in qs.all():
    print(r.name_upper)

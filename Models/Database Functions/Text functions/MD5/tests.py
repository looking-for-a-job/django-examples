#!/usr/bin/env python
from django.db.models.functions import MD5
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#md5

class MD5(expression, **extra)
"""

qs = MyModel.objects.annotate(name_md5=MD5('name'))
for r in qs.all():
    print(r.name_md5)

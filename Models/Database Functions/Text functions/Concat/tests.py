#!/usr/bin/env python
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#concat

class Concat(*expressions, **extra)
"""

qs = MyModel.objects.annotate(
    fullname=Concat('owner', V('/'), 'repo',
        output_field=CharField()
    )
)
for r in qs.all():
    print(r.fullname)

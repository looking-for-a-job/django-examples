#!/usr/bin/env python
import datetime
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#minute

DateTimeField, TimeField. 0..59
"""

qs = MyModel.objects
qs = q.filter(time__minute__gte=30)

for r in qs.all():
    print(r.time)

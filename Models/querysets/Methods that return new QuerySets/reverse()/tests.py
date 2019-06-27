#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#reverse

reverse()
"""

qs = MyModel.objects
qs = q.reverse()
for r in qs.all():
    print(r.title)

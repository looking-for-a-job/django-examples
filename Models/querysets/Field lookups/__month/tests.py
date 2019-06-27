#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#month

DateTimeField, DateField. 1..12
"""


qs = MyModel.objects
q.filter(field__month__gt=6)

#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#week

week number (1-52 or 53) according to ISO-8601
"""

qs = MyModel.objects

q.filter(field__week=3)       # =
q.filter(field__week__gt=3)   # >
q.filter(field__week__gte=3)  # >=
q.filter(field__week__lt=3)   # <
q.filter(field__week__lte=3)  # <=

q.filter(field__week__gte=32, field__week__lte=38)

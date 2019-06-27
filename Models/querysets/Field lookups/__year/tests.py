#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#year
"""

qs = MyModel.objects
year = datetime.now().year

q.filter(field__year=year)       # =
q.filter(field__year__gt=year)   # >
q.filter(field__year__gte=year)  # >=
q.filter(field__year__lt=year)   # <
q.filter(field__year__lte=year)  # <=

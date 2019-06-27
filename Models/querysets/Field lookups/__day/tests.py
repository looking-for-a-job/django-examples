#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#day

1..31
"""


qs = MyModel.objects
q.filter(field__day=3)      # =
q.filter(field__day__gt=3)  # >
q.filter(field__day__gte=3) # >=
q.filter(field__day__lt=3)  # <
q.filter(field__day__lte=3) # <=

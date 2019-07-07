#!/usr/bin/env python
from django.db.models import Q
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#or
"""

qs1=MyModel.objects.filter(x=1) | MyModel.objects.filter(y=2)
qs2=MyModel.objects.filter(Q(x=1) | Q(y=2))
assert str(qs1.query)==str(qs2.query)

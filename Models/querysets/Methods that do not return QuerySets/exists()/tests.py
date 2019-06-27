#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#exists
"""

qs = MyModel.objects.all()
if qs.filter(pk=42).exists():
    print("Entry contained in queryset")
if qs:
    print("There is at least one object in some_queryset")

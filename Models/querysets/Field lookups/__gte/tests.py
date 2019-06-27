#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#gte
"""

qs = MyModel.objects
q.filter(field__gte=42) # >=42

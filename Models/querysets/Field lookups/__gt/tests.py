#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#gt
"""

qs = MyModel.objects
q.filter(field__gt=42) # =42

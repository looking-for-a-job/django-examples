#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#lte
"""

qs = MyModel.objects
q.filter(field__lte=42) # <=42

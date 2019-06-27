#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#lt
"""

qs = MyModel.objects
q.filter(field__lt=42) # <42

#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#first
"""

obj = MyModel.objects.first()
if obj:
    print(obj)

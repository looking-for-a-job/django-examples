#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#last
"""

obj = MyModel.objects.last()
if obj:
    print(obj)

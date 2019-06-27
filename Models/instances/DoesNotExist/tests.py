#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist
"""

try:
    MyModel.objects.get(pk=1)
except MyModel.DoesNotExist:
    pass

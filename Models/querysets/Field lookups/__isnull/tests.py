#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#isnull
"""

qs = MyModel.objects
q.filter(field__isnull=False)
# equivalent to:
q.exclude(field__isnull=True)

#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#regex
"""

qs = MyModel.objects
qs = q.filter(field__regex=r'^(An?|The) +')

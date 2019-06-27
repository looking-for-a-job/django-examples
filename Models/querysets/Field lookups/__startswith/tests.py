#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#startswith
"""

qs = MyModel.objects

q.filter(field__startswith="startswith")

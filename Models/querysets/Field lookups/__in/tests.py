#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#in
"""


qs = MyModel.objects
q.filter(id__in=[1, 3, 4])

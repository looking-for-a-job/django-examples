#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#istartswith
"""

qs = MyModel.objects
q.filter(field__istartswith="istartswith")

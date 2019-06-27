#!/usr/bin/env python
from django.db import connection
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#defer

defer(*fields)
"""

qs = MyModel.objects.defer("field1", "field1").defer("field3")


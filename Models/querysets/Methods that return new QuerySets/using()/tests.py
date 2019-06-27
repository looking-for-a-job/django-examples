#!/usr/bin/env python
from django.db import connection
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#only

only(*fields)
"""

qs = Person.objects.only("name")
# equal to:
qs = Person.objects.defer("age", "biography")


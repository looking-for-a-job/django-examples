#!/usr/bin/env python
from django.db import connection
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#using

using(alias)
"""

# queries the database with the 'default' alias.
qs = MyModel.objects.all()

# queries the database with the 'backup' alias
MyModel.objects.using('backup')


#!/usr/bin/env python
from datetime import datetime
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#hour

DateTimeField, TimeField
"""



qs = Object.objects
print(q.filter(field__hour=23))
print(q.filter(field__hour__gte=12))

#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#quarter

DateTimeField, DateField. 1..4
"""

qs = MyModel.objects

q.filter(field__quarter=2) # second quarter (April 1 to June 30):

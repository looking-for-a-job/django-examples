#!/usr/bin/env python
import datetime
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#date

DateTimeField
"""

qs = MyModel.objects
date = datetime.date(2000, 1, 1)
q.filter(field__date=date)        # =
q.filter(field__date__gt=date)    # >
q.filter(field__date__gte=date)   # >=
q.filter(field__date__lt=date)    # <
q.filter(field__date__lte=date)   # <=

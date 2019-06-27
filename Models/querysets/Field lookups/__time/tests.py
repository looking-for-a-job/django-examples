#!/usr/bin/env python
import datetime
from .models import MyModel


"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#time

DateTimeField
"""


qs = MyModel.objects
q.filter(field__time=datetime.time(14, 30))
q.filter(field__time__range=(datetime.time(8), datetime.time(17)))


#!/usr/bin/env python
import datetime
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#range
"""


qs = MyModel.objects

start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2005, 3, 31)
q.filter(field__range=(start_date, end_date))

for r in qs.all():
    print(r.field)

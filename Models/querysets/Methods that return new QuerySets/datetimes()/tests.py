#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#datetimes

datetimes(field_name, kind, order='ASC', tzinfo=None)
"""

# kind: "year", "month", "week", "day", "hour", "minute", "second"
datetimes_by_second = list(MyModel.objects.datetimes('pub_date', 'second'))
print(datetimes_by_second)
datetimes_by_minute = list(MyModel.objects.datetimes('pub_date', 'minute'))
print(datetimes_by_minute)
datetimes_by_year = list(MyModel.objects.datetimes('pub_date', 'year'))
print(datetimes_by_year)

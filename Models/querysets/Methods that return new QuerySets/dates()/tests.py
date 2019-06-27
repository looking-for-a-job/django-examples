#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#dates

dates(field, kind, order='ASC')
"""

# kind: "year", "month", "week", "day"
dates = list(MyModel.objects.dates('pub_date', 'month'))
print(dates)

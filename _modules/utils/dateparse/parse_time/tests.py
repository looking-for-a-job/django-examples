#!/usr/bin/env python
from django.utils.dateparse import parse_date

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.dateparse.parse_time

parse_time(value)
"""


print(
    parse_date("2010-10-10"),
)

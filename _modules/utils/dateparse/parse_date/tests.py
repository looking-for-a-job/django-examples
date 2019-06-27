#!/usr/bin/env python
from django.utils.dateparse import parse_date

"""
https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.dateparse

parse_date(value)
"""

print(
    parse_date("2010-10-10"),
)

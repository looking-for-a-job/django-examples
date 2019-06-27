#!/usr/bin/env python
from django.utils.dateparse import parse_duration

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.dateparse.parse_datetime

parse_duration(value)

Parses a string and returns a datetime.timedelta.

Expects data in the format "DD HH:MM:SS.uuuuuu" or as specified by ISO 8601 (e.g. P4DT1H15M20S which is equivalent to 4 1:15:20) or PostgreSQL’s day-time interval format (e.g. 3 days 04:05:06
"""

print(
    parse_duration("1 12:10:30.01"),
)

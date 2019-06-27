#!/usr/bin/env python
from django.utils.timezone import get_default_timezone

"""
https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.timezone
"""

tz = get_default_timezone()
print(tz) # datetime.tzinfo subclass



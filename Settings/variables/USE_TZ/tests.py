#!/usr/bin/env python
from django.utils import timezone
import pytz

# UTC
timezone.utc

# custom timezone
melb = pytz.timezone('Australia/Melbourne')  # UTC+10:00
with timezone.override(melb):
    pass

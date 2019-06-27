#!/usr/bin/env python
from .models import Person

"""
https://docs.djangoproject.com/en/dev/topics/db/sql/
"""

for p in Person.objects.raw("SELECT *,'custom' as custom_field FROM person"):
    print(p.first_name, p.custom_field)


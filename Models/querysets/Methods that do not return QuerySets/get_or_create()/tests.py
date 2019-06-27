#!/usr/bin/env python
from datetime import date
from .models import Person

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#get-or-create

get_or_create(defaults=None, **kwargs)
"""

obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)

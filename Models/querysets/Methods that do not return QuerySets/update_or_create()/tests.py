#!/usr/bin/env python
from datetime import date
from .models import Person

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#update-or-create

update_or_create(defaults=None, **kwargs)
"""

obj, created = Person.objects.update_or_create(
    first_name='John', last_name='Lennon',
    defaults={'first_name': 'New name'},
)
assert obj.first_name == 'New name'

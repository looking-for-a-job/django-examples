#!/usr/bin/env python
from .models import Person

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#create

create(**kwargs)
"""

p = Person.objects.create(first_name="Bruce", last_name="Springsteen")

#!/usr/bin/env python
import django
from django.contrib.auth.models import User

"""
https://docs.djangoproject.com/en/dev/ref/models/meta/#django.db.models.options.Options.get_field

get_field(field_name)
"""

# A field from another model that has a relation with the current model
print(User._meta.get_field('logentry'))

# A field on the model
print(User._meta.get_field('username'))

try:
    User._meta.get_field('does_not_exist')
except django.core.exceptions.FieldDoesNotExist:
    pass

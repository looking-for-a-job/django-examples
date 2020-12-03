#!/usr/bin/env python
from django.contrib.auth.models import User

"""
https://docs.djangoproject.com/en/dev/ref/models/meta/#django.db.models.options.Options.get_fields

get_fields(include_parents=True, include_hidden=False)
"""

print("User fields(%s):" % len(User._meta.get_fields()))
for f in User._meta.get_fields():
    print(f)
print("\nUser fields(%s):" % len(User._meta.get_fields(include_hidden=True)))
for f in User._meta.get_fields(include_hidden=True):
    print(f)

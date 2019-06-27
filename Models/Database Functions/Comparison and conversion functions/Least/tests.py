#!/usr/bin/env python
from django.db.models.functions import Least
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#least

class Least(*expressions, **extra)

Accepts a list of at least two field names or expressions and returns the least value. Each argument must be of a similar type, so mixing text and numbers will result in a database error.
"""

qs = MyModel.objects.annotate(least=Least('a', 'b'))
for r in qs.all():
    print("%s (%s, %s)" % (r.least,r.a,r.b))

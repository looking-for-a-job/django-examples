#!/usr/bin/env python
from django.db.models.functions import Coalesce
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#coalesce

class Coalesce(*expressions, **extra)

Accepts a list of at least two field names or expressions and returns the first non-null value (note that an empty string is not considered a null value). Each argument must be of a similar type, so mixing text and numbers will result in a database error.
"""

qs = MyModel.objects.annotate(out=Coalesce('alias', 'name'))
for r in qs.all():
    print(r.out)

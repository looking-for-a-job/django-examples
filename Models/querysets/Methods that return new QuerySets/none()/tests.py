#!/usr/bin/env python
from django.db.models.query import EmptyQuerySet
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#none
"""

qs = MyModel.objects.none()
assert isinstance(q, EmptyQuerySet)==True
assert list(q)==[]

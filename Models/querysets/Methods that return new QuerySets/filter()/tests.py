#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#filter

filter(**kwargs)
"""

qs = MyModel.objects.filter(published=True)
print(qs.all())

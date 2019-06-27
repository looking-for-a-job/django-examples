#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#exclude

exclude(**kwargs)
"""

qs = MyModel.objects.exclude(published=True)
print(qs.all())

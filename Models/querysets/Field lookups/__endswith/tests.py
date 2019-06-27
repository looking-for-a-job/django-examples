#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#endswith
"""


qs = MyModel.objects
q.filter(field__endswith="endswith")

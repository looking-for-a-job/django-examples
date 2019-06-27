#!/usr/bin/env python
from django.db import models
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#all

objects         models.manager.Manager
objects.all()   models.query.QuerySet
"""

qs = MyModel.objects.all()


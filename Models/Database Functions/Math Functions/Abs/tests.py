#!/usr/bin/env python
from django.db.models.functions import Now
from .models import Vector

"""
https://docs.djangoproject.com/en/dev/ref/models/database-functions/#now

"""

qs = Article.objects.filter(published__lte=Now())

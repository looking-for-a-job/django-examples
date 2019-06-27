#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together

class UniqueConstraint(*, fields, name, condition=None)
"""

class MyModel(models.Model):
    room = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ['room', 'date']

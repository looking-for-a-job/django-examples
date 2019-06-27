#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/constraints/#uniqueconstraint

class UniqueConstraint(*, fields, name, condition=None)
"""

class MyModel(models.Model):
    Room = models.IntegerField()
    Date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Room','Date'],name='unique_booking'),
        ]

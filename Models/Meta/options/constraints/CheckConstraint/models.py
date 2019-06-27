#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/constraints/#checkconstraint

class CheckConstraint(*, check, name)
"""

class MyModel(models.Model):
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        ]

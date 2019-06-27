#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/topics/db/models/#meta-inheritance
"""

class CommonInfo(models.Model):
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'

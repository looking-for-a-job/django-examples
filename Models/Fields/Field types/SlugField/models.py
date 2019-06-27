#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/forms/fields/#slugfield
"""


class MyModel(models.Model):
    slug = models.SlugField()

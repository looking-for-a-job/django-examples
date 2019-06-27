#!/usr/bin/env python
from django.db import models

# https://docs.djangoproject.com/en/dev/ref/models/options/


class MyModel(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    owner = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)

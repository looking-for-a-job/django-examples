#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

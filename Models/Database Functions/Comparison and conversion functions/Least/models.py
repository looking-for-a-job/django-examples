#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()

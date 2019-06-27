#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    alias = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100)

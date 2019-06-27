#!/usr/bin/env python
from django.db import models

class Blog(models.Model):
    name = models.TextField()

class Entry(models.Model):
    name = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

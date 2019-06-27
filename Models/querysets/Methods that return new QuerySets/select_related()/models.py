#!/usr/bin/env python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()


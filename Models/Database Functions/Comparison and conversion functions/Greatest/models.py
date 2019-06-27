#!/usr/bin/env python
from django.db import models

class Blog(models.Model):
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

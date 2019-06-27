#!/usr/bin/env python
from django.db import models

class Person(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    biography = models.TextField()

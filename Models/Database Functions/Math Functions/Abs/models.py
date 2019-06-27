#!/usr/bin/env python
from django.db import models

class Article(models.Model):
    published = models.DateTimeField()

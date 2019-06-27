#!/usr/bin/env python
from django.db import models

class Entry(models.Model):
    headline = models.TextField()

#!/usr/bin/env python
from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=64)

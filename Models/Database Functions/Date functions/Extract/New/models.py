#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    start_datetime = models.DateTimeField()


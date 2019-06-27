#!/usr/bin/env python
from django.db import models

class MyModel(models.Model):
    pub_date = models.DateTimeField()

#!/usr/bin/env python
from django.db import models


class MyModel(models.Model):
    field = models.DateTimeField()

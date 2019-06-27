#!/usr/bin/env python
from django.db import models


class Model(models.Model):
    published = models.BooleanField()

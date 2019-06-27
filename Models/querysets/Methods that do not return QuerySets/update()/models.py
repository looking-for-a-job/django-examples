#!/usr/bin/env python
from django.db import models

class Entry(models.Model):
    pub_date = models.DateField()
    comments_on = models.BooleanField()

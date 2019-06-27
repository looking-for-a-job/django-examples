#!/usr/bin/env python
from django.db import models

class Entry(models.Model):
    pub_date = models.DateField()
    expire_date = models.DateField()

    class Meta:
        get_latest_by = ["pub_date"]

#!/usr/bin/env python
from django.db import models
import os


class MyModel(models.Model):
    def __init__(self, *args, **kwargs):
        super(MyModel, self).__init__(*args, **kwargs)
        self.old_value = self.value

    def save(self):
        if self.old_value != self.value:
            super(MyModel, self).save()

    class Meta():
        app_label = "app"

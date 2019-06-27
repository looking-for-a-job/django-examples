#!/usr/bin/env python
from django.core.exceptions import ValidationError
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.clean_fields
"""

class MyModel(models.Model):
    title = models.CharField(max_length=30)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if "you'll never believe" in self.title.lower():
            raise ValidationError('Sensationalist Clickbait Not Allowed')

    def save(self):
        self.clean()
        super(MyModel, self).__init__(*args, **kwargs)

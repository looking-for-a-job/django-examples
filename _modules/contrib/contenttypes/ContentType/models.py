from django.db import models
from taggit.managers import TaggableManager

"""
https://github.com/jazzband/django-taggit
"""

class Food(models.Model):
    name = models.CharField(max_length=100)
    tags = TaggableManager()

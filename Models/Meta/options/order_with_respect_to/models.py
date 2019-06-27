#!/usr/bin/env python
from django.db import models

"""
https://docs.djangoproject.com/en/dev/ref/models/options/#order-with-respect-to


"""

class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'question'

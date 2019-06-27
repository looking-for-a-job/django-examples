#!/usr/bin/env python
from django.db import models

# https://docs.djangoproject.com/en/dev/ref/models/options/

class Question(models.Model):
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta():
        app_label = "app"
        db_table = "schema.table"
        db_tablespace = "tablespace"
        get_latest_by = ['-priority', 'order_date'] # latest() method
        ordering = ['ordering']
        order_with_respect_to = 'question'

        permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

        verbose_name = _('Interval')
        verbose_name_plural = _('intervals')


print(Answer()._meta.label)

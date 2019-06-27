#!/usr/bin/env python
from django.db import models
import django
django.setup()


class Category(models.Model):
    name = models.CharField("product group", max_length=64)

    class Meta():
        app_label = "app"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="group")
    name = models.CharField("product name", max_length=128)
    price = models.DecimalField("cost", max_digits=10, decimal_places=2)

    class Meta():
        app_label = "app"


print(Category.objects.filter(name='ax').all().query)

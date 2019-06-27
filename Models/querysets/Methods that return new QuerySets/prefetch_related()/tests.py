#!/usr/bin/env python
from .models import Pizza, Topping

"""
https://docs.djangoproject.com/en/dev/ref/models/querysets/#prefetch-related

prefetch_related(*lookups)
"""

qs = Pizza.objects.all().prefetch_related('toppings')
for pizza in qs.all():
    str(pizza) # self.toppings.all() are cached



#!/usr/bin/env python
from .models import MyModel

"""
https://docs.djangoproject.com/en/dev/ref/models/instances/#deleting-objects

Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)
"""

instance = MyModel(title='title1').save()

count, models = MyModel.objects.all().delete()
print("%s models deleted: %s" % (count, models))


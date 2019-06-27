#!/usr/bin/env python
from django.test import TestCase
from .models import MyModel


"""
https://docs.djangoproject.com/en/dev/ref/models/instances/#refreshing-objects-from-database
"""

class Test(TestCase):
    def test_update_result(self):
        obj = MyModel.objects.create(val=1)
        MyModel.objects.filter(pk=obj.pk).update(val=42)
        obj.refresh_from_db()
        self.assertEqual(obj.val, 42)

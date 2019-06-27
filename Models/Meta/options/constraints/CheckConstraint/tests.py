#!/usr/bin/env python
import django
from django.test import TestCase
from .models import MyModel

class Test(TestCase):
    def test_ok(self):
        MyModel(age=18).save()

    def test_exception(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            MyModel(age=11).save()

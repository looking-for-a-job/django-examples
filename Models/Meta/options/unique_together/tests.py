#!/usr/bin/env python
import datetime
import django
from django.test import TestCase
from .models import MyModel

class Test(TestCase):
    def test(self):
        date = datetime.datetime.now().today()
        MyModel(room=42,date=date).save()
        with self.assertRaises(django.db.utils.IntegrityError):
            MyModel(room=42,date=date).save()


#!/usr/bin/env python
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import MyModel


class Test(TestCase):
    def test_ok(self):
        obj = MyModel(title='title1')
        obj.clean_fields()
        obj.save()

    def test_ValidationError(self):
        with self.assertRaises(ValidationError):
            obj = MyModel(title="you'll never believe ...")
            obj.clean_fields()
            obj.save()

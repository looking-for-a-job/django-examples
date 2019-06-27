from django.urls import resolve
from django.urls.exceptions import Resolver404
from django.test import TestCase
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/topics/http/urls/#path-converters

resolve(path, urlconf=None)
"""

class Test(TestCase):
    def test_ok(self):
        match = resolve('/view-path/')
        self.assertEqual(match.func, my_view)
        self.assertEqual(match.url_name, 'view-name')

    def test_NoReverseMatch(self):
        with self.assertRaises(Resolver404):
            resolve('/invalid-path/')

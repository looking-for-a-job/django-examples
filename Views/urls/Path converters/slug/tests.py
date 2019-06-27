from django.urls import resolve
from django.urls.exceptions import Resolver404
from django.test import TestCase
from .views import my_view


class Test(TestCase):
    def test_ok(self):
        match = resolve('/path/')
        self.assertEqual(match.func, my_view)

    def test_NoReverseMatch(self):
        with self.assertRaises(Resolver404):
            resolve('/42/')

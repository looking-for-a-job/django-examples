from django.urls import resolve
from django.urls.exceptions import Resolver404
from django.test import TestCase
from . import views


class Test(TestCase):
    def test_special_case_2003(self):
        match = resolve('/articles/2003/')
        self.assertEqual(match.func, views.special_case_2003)

    def test_year_archive(self):
        match = resolve('/articles/2008/')
        self.assertEqual(match.func, views.year_archive)

    def test_year_archive(self):
        match = resolve('/articles/2008/12/')
        self.assertEqual(match.func, views.month_archive)

    def test_article_detail(self):
        match = resolve('/articles/2008/12/title/')
        self.assertEqual(match.func, views.article_detail)

    def test_NoReverseMatch(self):
        with self.assertRaises(Resolver404):
            resolve('/invalid-path/')

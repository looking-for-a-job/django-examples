from django.http import HttpResponse
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.charset
"""


class Test(TestCase):
    def test(self):
        response = HttpResponse(charset="utf-8")
        self.assertEqual(response.charset,"utf-8")

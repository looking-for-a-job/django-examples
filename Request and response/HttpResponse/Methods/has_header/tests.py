from django.urls import reverse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.has_header

has_header(header)
"""


class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        if not response.has_header('Last-Modified'):
            pass

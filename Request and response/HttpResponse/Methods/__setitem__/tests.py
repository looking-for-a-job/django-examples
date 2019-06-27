from django.urls import reverse
from django.http import HttpResponse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.__setitem__

__setitem__(header, value)
"""


class Test(TestCase):
    def test(self):
        response = HttpResponse()
        response['Cache-Control'] = 'no-cache'
        self.assertEqual(response['Cache-Control'],'no-cache')


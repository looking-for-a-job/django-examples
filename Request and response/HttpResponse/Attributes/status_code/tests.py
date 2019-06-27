from django.http import HttpResponse
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.status_code
"""


class Test(TestCase):
    def test(self):
        response = HttpResponse(status=201)
        self.assertEqual(response.status_code,201)

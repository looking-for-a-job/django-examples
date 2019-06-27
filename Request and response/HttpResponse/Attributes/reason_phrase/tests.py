from django.http import HttpResponse
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.reason_phrase
"""


class Test(TestCase):
    def test_default_reason(self):
        response = HttpResponse(status=201)
        self.assertEqual(response.reason_phrase,"Created")

    def test_custom_reason(self):
        response = HttpResponse(status=201,reason="Already exists")
        self.assertEqual(response.reason_phrase,"Already exists")


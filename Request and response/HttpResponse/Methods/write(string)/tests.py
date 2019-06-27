from django.urls import reverse
from django.http import HttpResponse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.has_header

has_header(header)
"""


class Test(TestCase):
    def test(self):
        response = HttpResponse()
        response.write("<p>Here's the text of the Web page.</p>")
        response.write("<p>Here's another paragraph.</p>")
        print(response.content)

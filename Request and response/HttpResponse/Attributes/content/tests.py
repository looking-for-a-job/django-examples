from django.http import HttpResponse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.content
"""


class Test(TestCase):
    def setUp(self):
        self.response = HttpResponse()

    def test(self):
        self.response.write("<p>Here's the text of the Web page.</p>")
        self.response.write("<p>Here's another paragraph.</p>")
        content = self.response.content.decode()
        self.assertEqual(content, "<p>Here's the text of the Web page.</p><p>Here's another paragraph.</p>")


from django.urls import reverse
from django.http import HttpResponse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.writelines

writelines(lines)
"""


class Test(TestCase):
    def test(self):
        response = HttpResponse()
        response.writelines(["line1","line2"])
        response.writelines(["line3","line4"])
        content = response.content.decode()
        self.assertEqual(content,"line1line2line3line4")

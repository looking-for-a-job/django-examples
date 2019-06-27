from django.http import HttpResponse
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.__init__

__init__(content=b'', content_type=None, status=200, reason=None, charset=None)
"""


class Test(TestCase):
    def test(self):
        content = "content string"
        content_type='text/html'
        status=500
        charset="utf-8"
        response = HttpResponse(content,content_type=content_type,status=status,charset=charset)
        self.assertEqual(response.content.decode(),content)
        self.assertEqual(response._headers['content-type'][1],content_type)
        self.assertEqual(response.status_code,status)
        self.assertEqual(response.charset,charset)

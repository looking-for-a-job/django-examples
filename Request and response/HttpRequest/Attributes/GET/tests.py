from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.GET
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get("/path?print=true&k=v")
        self.assertEqual(request.GET['print'],'true')
        self.assertEqual(request.GET['k'],'v')
        self.assertEqual(dict(request.GET),dict(print='true',k='v'))

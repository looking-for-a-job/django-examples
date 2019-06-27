from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.META
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get("/")
        print("request = %s" % str(request))
        print("request.__dict__ = %s" % str(request.__dict__))

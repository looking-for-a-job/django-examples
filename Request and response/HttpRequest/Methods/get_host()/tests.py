from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.get_host
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get("/")
        print(request.get_host())

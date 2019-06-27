from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.method
"""

class Test(TestCase):
    def test_get(self):
        request = RequestFactory().get("/")
        self.assertEqual(request.method,'GET')

    def test_post(self):
        request = RequestFactory().post("/",dict(k="v"))
        self.assertEqual(request.method,'POST')

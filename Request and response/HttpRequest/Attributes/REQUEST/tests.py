from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.REQUEST
"""

class Test(TestCase):
    def test_get(self):
        request = RequestFactory().get("/")
        self.assertEqual(request.REQUEST,request.GET)

    def test_post(self):
        request = RequestFactory().post("/",dict(key="value",key2=[1,2,3]))
        self.assertEqual(request.REQUEST,request.POST)

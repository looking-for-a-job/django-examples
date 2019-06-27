from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.POST
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().post("/",dict(key="value",key2=[1,2,3]))
        self.assertEqual(request.POST.get("key"),"value")
        self.assertEqual(request.POST.get("not-existing","default"),"default")

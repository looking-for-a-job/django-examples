from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.get_full_path
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get("/music/bands/the_beatles/?print=true")
        self.assertEqual(request.path,"/music/bands/the_beatles/?print=true")

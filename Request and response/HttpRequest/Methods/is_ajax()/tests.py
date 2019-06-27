from django.test import RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.is_ajax
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().post('/', {}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(request.is_ajax(),True)

        request = RequestFactory().post('/', {})
        self.assertEqual(request.is_ajax(),False)

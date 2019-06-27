from django.test import RequestFactory, TestCase
from .views import my_view

class Test(TestCase):
    def test_get(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        self.assertEqual(response.status_code, 200)

    def test_head(self):
        request = RequestFactory().head('/')
        response = my_view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post('/')
        response = my_view(request)
        self.assertEqual(response.status_code, 405)


from django.test import RequestFactory, TestCase
from .views import my_view

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        self.assertEqual(response._headers['cache-control'], ('Cache-Control', 'max-age=0, no-cache, no-store, must-revalidate'))


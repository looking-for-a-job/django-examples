from django.utils.cache import get_max_age
from django.test import RequestFactory, TestCase
from .views import my_view


class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        self.assertIn('must-revalidate',response._headers['cache-control'][1])
        self.assertEqual(get_max_age(response),3600)

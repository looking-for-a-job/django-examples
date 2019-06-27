from django.test import RequestFactory, TestCase
from django.utils.cache import get_max_age
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.cache.get_max_age

get_max_age(response)
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        self.assertEqual(get_max_age(response),3600)

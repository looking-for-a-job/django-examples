from django.test import RequestFactory, TestCase
from django.utils.cache import get_max_age, patch_response_headers
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.cache.patch_response_headers

patch_response_headers(response, cache_timeout=None)
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        patch_response_headers(response, cache_timeout=3600)
        self.assertEqual(get_max_age(response),3600)
        expires = response._headers["expires"][1]
        print(expires)

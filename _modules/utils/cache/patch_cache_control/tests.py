from django.test import RequestFactory, TestCase
from django.utils.cache import get_max_age, patch_cache_control
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.cache.patch_cache_control

patch_cache_control(response, **kwargs)
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        max_age = 3600
        patch_cache_control(response, max_age=max_age)
        self.assertEqual(get_max_age(response),max_age)

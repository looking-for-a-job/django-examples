from django.test import RequestFactory, TestCase
from django.utils.cache import add_never_cache_headers, get_max_age
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.cache.add_never_cache_headers

add_never_cache_headers(response)
"""

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        add_never_cache_headers(response)
        cache_control = response._headers["cache-control"]
        print("%s: %s" % (cache_control[0],cache_control[1]))

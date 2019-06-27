from django.http import QueryDict
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.popitem

popitem()
"""

class Test(TestCase):
    def test(self):
        qs = QueryDict('a=1&a=2&a=3', mutable=True)
        self.assertEqual(q.popitem(), ('a', ['1', '2', '3']))

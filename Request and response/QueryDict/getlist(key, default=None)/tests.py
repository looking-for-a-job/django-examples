from django.http import QueryDict
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.getlist

getlist(key, default=None)
"""

class Test(TestCase):
    def test(self):
        qs = QueryDict('a=1&a=2&c=3')
        self.assertEqual(q.getlist("a"), ['1', '2'])

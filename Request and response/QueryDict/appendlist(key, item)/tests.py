from django.http import QueryDict
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.appendlist

appendlist(key, item)
"""

class Test(TestCase):
    def test(self):
        qs = QueryDict('a=1&a=2&c=3',mutable=True)
        q.appendlist('a','4')
        self.assertEqual(q.getlist("a"), ['1', '2', '4'])

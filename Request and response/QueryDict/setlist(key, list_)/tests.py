from django.http import QueryDict
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.setlist
setlist(key, list_)
"""

class Test(TestCase):
    def test(self):
        qs = QueryDict('a=1&a=2&c=3',mutable=True)
        q.setlist("a",['1','4'])
        self.assertEqual(q.getlist("a"), ['1', '4'])

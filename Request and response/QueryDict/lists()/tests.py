from django.http import QueryDict
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.lists

lists()
"""

class Test(TestCase):
    def test(self):
        qs = QueryDict('a=1&a=2&c=3')
        self.assertEqual(list(q.lists()),[('a', ['1', '2']), ('c', ['3'])])

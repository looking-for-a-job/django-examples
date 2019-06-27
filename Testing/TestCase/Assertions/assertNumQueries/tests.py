from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertNumQueries

assertNumQueries(num, func, *args, **kwargs)
"""

class Test(TestCase):
    def test(self):
        raise NotImplementedError

from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertContains

assertContains(response, text, count=None, status_code=200, msg_prefix='', html=False)
assertNotContains(response, text, status_code=200, msg_prefix='', html=False)
"""

class Test(TestCase):
    def test(self):
        raise NotImplementedError

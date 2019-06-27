from django.conf import settings
from django.test import TestCase


"""
https://docs.djangoproject.com/en/2.2/topics/testing/tools/#django.test.SimpleTestCase.settings
"""

class Test(TestCase):
    def test(self):
        with self.settings(DEBUG=False):
            self.assertEqual(settings.DEBUG,False)


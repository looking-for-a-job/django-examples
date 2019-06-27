from django.conf import settings
from django.test import TestCase, override_settings

"""
https://docs.djangoproject.com/en/2.2/topics/testing/tools/#django.test.override_settings
"""

class Test(TestCase):
    @override_settings(DEBUG=False)
    def test(self):
        self.assertEqual(settings.DEBUG,False)

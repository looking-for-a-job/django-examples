from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertWarnsMessage

assertWarnsMessage(expected_warning, expected_message, callable, *args, **kwargs)
assertWarnsMessage(expected_warning, expected_message)
"""

class Test(TestCase):
    def test(self):
        raise NotImplementedError

from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertRaisesMessage

assertRaisesMessage(expected_exception, expected_message, callable, *args, **kwargs)
assertRaisesMessage(expected_exception, expected_message)
"""

class Test(TestCase):
    def test(self):
        with self.assertRaisesMessage(ValueError, 'invalid literal for int()'):
            int('a')

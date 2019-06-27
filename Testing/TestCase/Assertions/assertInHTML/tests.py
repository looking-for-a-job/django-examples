from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertInHTML

assertInHTML(needle, haystack, count=None, msg_prefix='')
"""

class Test(TestCase):
    def test(self):
        self.assertInHTML('<p>hello</p>', '<div><p>hello</p><p>b</p></div>')

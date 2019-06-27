from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertRedirects

assertRedirects(response, expected_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
"""

class Test(TestCase):
    def test(self):
        self.assertInHTML('<p>hello</p>', '<div><p>hello</p><p>b</p></div>')

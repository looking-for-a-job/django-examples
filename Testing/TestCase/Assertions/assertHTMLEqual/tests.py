from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertHTMLEqual

assertHTMLEqual(html1, html2, msg=None)
assertHTMLNotEqual(html1, html2, msg=None)
"""

class Test(TestCase):
    def test(self):
        self.assertHTMLEqual(
            '<p>Hello <b>world!</p>',
            '''<p>
                Hello   <b>world! </b>
            </p>'''
        )
        self.assertHTMLEqual(
            '<input type="checkbox" checked="checked" id="id_accept_terms" />',
            '<input id="id_accept_terms" type="checkbox" checked>'
        )

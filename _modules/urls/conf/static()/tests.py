from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.test import TestCase

"""
https://docs.djangoproject.com/en/dev/ref/urls/#static

static(prefix, view=django.views.static.serve, **kwargs)
"""

class Test(TestCase):
    def test_ok(self):
        path = reverse('view-name')
        self.assertEqual(path,'/view-path/')

    def test_NoReverseMatch(self):
        with self.assertRaises(NoReverseMatch):
            reverse('invalid-view-name')



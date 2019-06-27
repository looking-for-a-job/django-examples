from django.urls import reverse
from django.test import Client, TestCase

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TestCase.assertTemplateUsed

assertTemplateUsed(response, template_name, msg_prefix='', count=None)
"""

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

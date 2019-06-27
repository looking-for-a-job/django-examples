from django.urls import reverse
from django.test import Client, TestCase

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

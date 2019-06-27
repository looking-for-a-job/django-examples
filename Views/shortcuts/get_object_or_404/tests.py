from django.urls import reverse
from django.test import Client, TestCase
from .models import Model

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 404)

from django.urls import reverse
from django.test import Client, TestCase

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        response = self.client.get('/')
        content = response.content.decode()
        print(content)

from django.test import Client, TestCase
from .models import Post

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        for i in range(10):
            Post(title="article title%s" % i).save()
        response = self.client.get('')
        content = response.content.decode()
        print(content)

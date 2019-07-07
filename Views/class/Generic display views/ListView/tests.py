from django.test import Client, TestCase
from .models import Article

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        for i in range(10):
            Article(headline="article headline%s" % i,content="content%s" % i).save()
        response = self.client.get('')
        content = response.content.decode()
        print(content)

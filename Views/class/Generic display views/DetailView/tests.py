from django.test import Client, TestCase
from .models import Article

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        article = Article(title="article title")
        article.save()

        url = "/%s/" % article.slug
        response = self.client.get(url)
        content = response.content.decode()
        print(content)

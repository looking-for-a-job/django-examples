from django.test import  TestCase
from .forms import ArticleForm
from .models import Article

class Test(TestCase):
    def test(self):
        article = Article(headline="headline",content="content")
        form = ArticleForm(initial={'headline': 'overrided headline'}, instance=article)
        self.assertEqual(form['headline'].value(), 'overrided headline')


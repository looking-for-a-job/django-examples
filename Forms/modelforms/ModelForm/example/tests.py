from django.test import  TestCase
from .forms import ArticleForm
from .models import Article

class Test(TestCase):
    def setUp(self):
        Article(headline="headline",content="content").save()

    def test(self):
        form = ArticleForm()

        article = Article.objects.get(pk=1)
        form = ArticleForm(instance=article)
        print(form)


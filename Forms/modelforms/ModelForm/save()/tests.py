from django.test import RequestFactory, TestCase
from .forms import ArticleForm
from .models import Article

"""
https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#the-save-method
"""

class Test(TestCase):
     def setUp(self):
        self.factory = RequestFactory()
        Article(headline="headline",content="content").save()

    def test_create(self):
        request = self.factory.post('/',{'headline':'title','content': 'content'})
        f = ArticleForm(request.POST)
        new_article = f.save()

    def test_update(self):
        request = self.factory.post('/',{'headline':'title2','content': 'content2'})
        article = Article.objects.get(pk=1)
        f = ArticleForm(request.POST, instance=article)
        updated_article = f.save()

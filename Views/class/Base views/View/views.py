from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from articles.models import Article

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#redirectview
"""



class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)

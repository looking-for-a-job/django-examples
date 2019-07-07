from django.http import Http404
from django.views.generic.detail import DetailView
from .models import Article

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#detailview
"""

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article" # default is "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

"""
    def get_object(self):
        object = super(ArticleDetailView, self).get_object()
        if not self.request.user.is_authenticated():
            raise Http404
        return object
 """

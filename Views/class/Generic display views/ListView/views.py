from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Article

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
"""

class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list" # default is "object_list"
    paginate_by = 5  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

"""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Article.objects.filter(is_private=True, is_deleted=False)
"""

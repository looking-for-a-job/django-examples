from django.urls import path
from django.views.generic.base import RedirectView

from .views import ArticleCounterRedirectView, ArticleDetail

urlpatterns = [
    path('counter/<int:pk>/', ArticleCounterRedirectView.as_view(), name='article-counter'),
    path('details/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]

from django.urls import path
from . import views

"""
https://docs.djangoproject.com/en/dev/topics/http/urls/#path-converters
"""

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]

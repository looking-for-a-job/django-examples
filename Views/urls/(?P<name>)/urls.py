#!/usr/bin/env python
from django.conf.urls import patterns
from django.http import HttpResponse

def articles_2003(request):
    return HttpResponse(request.path)

urlpatterns = patterns('',
    (r'^articles/2003/$', articles_2003),
    (r'^articles/(\d{4})/$', 'news.views.year_archive'),
    (r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
    (r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),
)
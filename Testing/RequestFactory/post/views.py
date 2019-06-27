#!/usr/bin/env python
from django.http import HttpResponse


def my_view(request):
    return HttpResponse("title = %s" % request.POST['title'])

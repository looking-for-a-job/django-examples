#!/usr/bin/env python
from django.http import HttpResponse, HttpResponseNotFound


def my_view(request):
    return HttpResponse('hello world')

def handler404(request, *args, **kwargs):
    """works only with DEBUG = False
    """
    return HttpResponseNotFound("handler404 output")


#!/usr/bin/env python
from django.http import HttpResponse


def my_view(request):
    return HttpResponse("return this string")

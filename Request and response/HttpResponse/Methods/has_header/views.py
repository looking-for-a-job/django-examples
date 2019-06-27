#!/usr/bin/env python
from django.http import HttpResponse


def view(request):
    return HttpResponse("return this string")

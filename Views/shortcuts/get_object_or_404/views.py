#!/usr/bin/env python
import django
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Model

"""
https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#django.shortcuts.get_object_or_404

get_object_or_404(klass, *args, **kwargs)
"""


def view(request):
    obj = get_object_or_404(Model,pk=1)
    # equivalent to:
    try:
        obj = Model.objects.get(pk=1)
    except Model.DoesNotExist:
        raise Http404("No Model matches the given query.")

#!/usr/bin/env python
import django
from django.http import Http404
from django.shortcuts import get_list_or_404
from .models import Model

"""
https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#django.shortcuts.get_list_or_404

get_list_or_404(klass, *args, **kwargs)
"""


def view(request):
    objects = get_list_or_404(Model, published=True)
    # equivalent to:
    objects = list(MyModel.objects.filter(published=True))
    if not objects:
        raise Http404("No MyModel matches the given query.")

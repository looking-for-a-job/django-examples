#!/usr/bin/env python
import django
from django.shortcuts import redirect
from .models import Model

"""
https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#redirect

redirect(to, *args, permanent=False, **kwargs)
"""


class View(django.views.View):
    def get(self, request, *args, **kwargs):
        obj = Model.objects.get(title="title")
        return redirect(obj)

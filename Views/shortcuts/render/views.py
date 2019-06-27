#!/usr/bin/env python
import django
from django.shortcuts import render

"""
https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#render

render(request, template_name, context=None, content_type=None, status=None, using=None)
"""


class View(django.views.View):
    def get(self, request, *args, **kwargs):
        return render(self.request, "index.html", {})

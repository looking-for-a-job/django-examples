#!/usr/bin/env python
from django.http import Http404
from django.shortcuts import render
from .models import Poll

"""
https://docs.djangoproject.com/en/dev/topics/http/views/#the-http404-exception
"""

def my_view(request,poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})

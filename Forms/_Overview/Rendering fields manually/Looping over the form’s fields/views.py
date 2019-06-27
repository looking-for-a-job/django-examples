#!/usr/bin/env python
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    form = MyForm()
    return render(request, "index.html", {"form":form})

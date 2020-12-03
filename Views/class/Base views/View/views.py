from django.http import HttpResponse
from django.views import View

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#view
"""

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

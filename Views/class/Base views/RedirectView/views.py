from django.http import HttpResponse
from django.views import View

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#view
"""

class MyView(View):
    http_method_names = ["get","post"]
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

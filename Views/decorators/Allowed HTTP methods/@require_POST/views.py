from django.http import HttpResponse
from django.views.decorators.http import require_POST

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.require_POST

POST only
"""

@require_POST
def my_view(request):
    return HttpResponse("return this string")

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#django.views.generic.base.View.http_method_names
"""

class MyView(View):
    http_method_names = ["post"]

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

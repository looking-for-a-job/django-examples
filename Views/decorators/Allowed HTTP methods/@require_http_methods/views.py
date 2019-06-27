from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.require_http_methods
"""

@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse("return this string")

"""
https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#django.views.generic.base.View.http_method_names
"""

class MyView(View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

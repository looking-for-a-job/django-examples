from django.http import HttpResponse
from django.views.decorators.cache import cache_control


@cache_control(max_age=3600)
def my_view(request):
    return HttpResponse("return this string")

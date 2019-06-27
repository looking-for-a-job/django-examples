from django.http import HttpResponse
from django.views.decorators.cache import never_cache

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.cache.never_cache

Cache-Control: max-age=0, no-cache, no-store, must-revalidate
"""

@never_cache
def my_view(request):
    return HttpResponse("return this string")

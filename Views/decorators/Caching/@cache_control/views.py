from django.http import HttpResponse
from django.views.decorators.cache import cache_control

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.cache.cache_control

public=True
private=True
no_cache=True
no_transform=True
must_revalidate=True
proxy_revalidate=True
max_age=num_seconds
s_maxage=num_seconds
"""

@cache_control(must_revalidate=True, max_age=3600)
def my_view(request):
    return HttpResponse("return this string")

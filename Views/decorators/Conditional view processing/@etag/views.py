import hashlib
from django.http import HttpResponse
from django.views.decorators.http import etag

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.etag
"""

def my_etag(request, *args, **kwargs):
    return hashlib.md5(':'.join(request.GET.dict().values()).encode('utf-8')).hexdigest()

@etag(my_etag)
def my_view(request):
    return HttpResponse("return this string")


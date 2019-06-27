import hashlib
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.http import condition

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.condition
"""

def my_etag(request, *args, **kwargs):
    return hashlib.md5(':'.join(request.GET.dict().values()).encode('utf-8')).hexdigest()

def my_last_modified(request, *args, **kwargs):
    return datetime(2019, 1, 1)

@condition(etag_func=my_etag, last_modified_func=my_last_modified)
def my_view(request):
    return HttpResponse("return this string")


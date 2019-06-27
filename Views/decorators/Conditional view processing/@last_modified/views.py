from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.http import last_modified

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.last_modified
"""

def my_last_modified(request, *args, **kwargs):
    return datetime(2019, 1, 1)


@last_modified(my_last_modified)
def my_view(request):
    return HttpResponse("return this string")

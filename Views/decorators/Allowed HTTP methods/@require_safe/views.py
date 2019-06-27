from django.http import HttpResponse
from django.views.decorators.http import require_safe

"""
https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.require_safe

GET and HEAD only
"""

@require_safe
def my_view(request):
    return HttpResponse("return this string")

from django.urls import path
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/topics/http/urls/#path-converters
"""

urlpatterns = [
    path('<slug:path>/', my_view)
]

from django.test import RequestFactory
from .views import my_view

request = RequestFactory().get('/')
response = my_view(request)
etag = response._headers["etag"][1]

print("etag = %s" % etag)

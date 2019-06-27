from django.test import RequestFactory
from .views import my_view

request = RequestFactory().get('/')
response = my_view(request)
last_modified=response._headers["last-modified"][1] # Tue, 01 Jan 2019 00:00:00 GMT
etag = response._headers["etag"][1]

print("last_modified = %s" % last_modified)
print("etag = %s" % etag)

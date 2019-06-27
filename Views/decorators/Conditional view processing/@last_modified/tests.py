from django.test import RequestFactory
from .views import my_view

request = RequestFactory().get('/')
response = my_view(request)
print(response._headers["last-modified"][1]) # Tue, 01 Jan 2019 00:00:00 GMT

from django.test import TestCase
from django.test.client import RequestFactory
from .views import my_view

class Test(TestCase):
    def test(self):
        request = RequestFactory().get('/')
        response = my_view(request)
        print(response.content.decode())

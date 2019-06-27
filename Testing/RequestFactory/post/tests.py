from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/topics/testing/advanced/#the-request-factory
"""

class Test(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.post('/',{'title':'value'})
        response = my_view(request)
        self.assertEqual(dict(request.POST), {'title': ['value']})
        print(response)

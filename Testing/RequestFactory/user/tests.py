from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import my_view

"""
https://docs.djangoproject.com/en/dev/topics/testing/advanced/#the-request-factory
"""

class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', email='ya@ya.ru', password='xxx')

    def test(self):
        request = RequestFactory().get('/')
        request.user = self.user # simulate a logged-in user
        request.user = AnonymousUser() # simulate an anonymous user

        response = my_view(request)

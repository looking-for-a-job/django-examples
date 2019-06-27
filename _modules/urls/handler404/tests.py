from django.test import Client, override_settings, RequestFactory, TestCase

"""
https://docs.djangoproject.com/en/dev/ref/urls/#handler404

reverse(viewnamoverride_settings, urlconf=None, args=None, kwargs=None, current_app=None)
"""

class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_handler404(self):
        response = self.client.get('/invalid-path/')
        self.assertEqual(response.status_code,404)
        self.assertEqual(response.content.decode(),"handler404 output")

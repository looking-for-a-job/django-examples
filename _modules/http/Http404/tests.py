from django.test import Client, override_settings, RequestFactory, TestCase


class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_handler404(self):
        response = self.client.get('/42/')
        # self.assertEqual(response.status_code,404)
        print(response.content.decode())

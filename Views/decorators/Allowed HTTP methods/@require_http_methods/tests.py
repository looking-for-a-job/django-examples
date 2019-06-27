from django.test import RequestFactory, TestCase
from .views import my_view, MyView

class Test(TestCase):
    def test_get(self):
        request = RequestFactory().get('/')
        for view in [my_view,MyView.as_view()]:
            response = view(request)
            self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post('/')
        for view in [my_view,MyView.as_view()]:
            response = view(request)
            self.assertEqual(response.status_code, 200)

    def test_patch(self):
        request = RequestFactory().patch('/')
        for view in [my_view,MyView.as_view()]:
            response = view(request)
            self.assertEqual(response.status_code, 405)


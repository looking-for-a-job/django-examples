from django.test import  TestCase
from .forms import Form

class Test(TestCase):
    def test_view(self):
        form = Form()
        print(form.as_ul())
        # {{ form.as_ul }}


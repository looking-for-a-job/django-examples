from django.test import  TestCase
from .forms import MyForm

"""
https://docs.djangoproject.com/en/dev/ref/forms/api/#django.forms.Form.clean
"""

class Test(TestCase):
    def test_not_valid(self):
        form = MyForm({'title':'?'})
        self.assertEqual(form.is_valid(),False)

    def test_valid(self):
        form = MyForm({'title':'good title'})
        self.assertEqual(form.is_valid(),True)

from django.test import  TestCase
from .forms import MyForm

"""
https://docs.djangoproject.com/en/dev/ref/forms/api/#django.forms.Form.is_bound
"""

class Test(TestCase):
    def test_not_bound(self):
        form = MyForm()
        self.assertEqual(form.is_bound,False)

    def test_bound(self):
        form = MyForm({'title':'title value'})
        self.assertEqual(form.is_bound,True)

        form = MyForm({})
        self.assertEqual(form.is_bound,True)

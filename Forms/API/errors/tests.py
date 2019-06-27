from django.test import  TestCase
from .forms import MyForm

"""
https://docs.djangoproject.com/en/dev/ref/forms/api/#django.forms.Form.errors
"""

form = MyForm({'subject':'','sender':'invalid-email'})
print(form.errors)
print(form.errors.as_data())
# {'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}

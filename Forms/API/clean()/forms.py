from django import forms

"""
https://docs.djangoproject.com/en/dev/ref/forms/api/#django.forms.Form.clean

clean() called by form.is_valid()
"""

class MyForm(forms.Form):
    title = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if len(title)<5:
            raise forms.ValidationError("title is too short")

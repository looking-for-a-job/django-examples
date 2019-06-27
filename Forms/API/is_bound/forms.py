from django import forms

class MyForm(forms.Form):
    title = forms.CharField(max_length=100)

from django import forms


class MyForm(forms.Form):
    subject = forms.CharField(max_length=100,required=True)
    sender = forms.EmailField()

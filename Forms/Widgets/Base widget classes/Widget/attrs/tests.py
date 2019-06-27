from django import forms

"""
https://docs.djangoproject.com/en/dev/ref/forms/widgets/#django.forms.Widget.attrs
"""

name = forms.TextInput(attrs={'size': 10, 'title': 'title string'})
html = name.render('name', 'value string')
print(html)

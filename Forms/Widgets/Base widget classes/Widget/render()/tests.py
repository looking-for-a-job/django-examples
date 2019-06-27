from django import forms

"""
https://docs.djangoproject.com/en/dev/ref/forms/widgets/#django.forms.Widget.render

render(name, value, attrs=None, renderer=None)
"""

name = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
html = name.render('name', 'A name',attrs={'size': 42})
print(html)

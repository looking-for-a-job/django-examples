from django import forms


name = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
html = name.render('name', 'A name')
print(html)

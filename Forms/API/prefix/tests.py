from .forms import PersonForm

"""
https://docs.djangoproject.com/en/dev/ref/forms/api/#django.forms.Form.prefix
"""

mother = PersonForm(prefix="mother")
father = PersonForm(prefix="father")

print(mother.as_ul(),"\n")
print(father.as_ul())

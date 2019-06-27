from django.forms import modelform_factory
from .models import Article

"""
https://docs.djangoproject.com/en/dev/ref/forms/models/#modelform-factory

modelform_factory(model, form=ModelForm, fields=None, exclude=None, formfield_callback=None, widgets=None, localized_fields=None, labels=None, help_texts=None, error_messages=None, field_classes=None)
"""

Form = modelform_factory(Article, fields=("pub_date", "headline", "content"))



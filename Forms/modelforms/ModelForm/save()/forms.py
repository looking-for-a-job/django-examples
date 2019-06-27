from django.forms import ModelForm
from .models import Article

"""
https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#the-save-method
"""

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

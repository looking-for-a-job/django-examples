from django.forms import ModelForm
from .models import Article

"""
https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelform
"""

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content'] # '__all__'
        exclude = ['updated_at']

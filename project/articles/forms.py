from django import forms
from .models import *
from django.forms import ModelForm


class ArticleForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = ArticleModel
        fields = '__all__'
        exclude = ['article_author', 'article_slug', 'article_totalViewCount']

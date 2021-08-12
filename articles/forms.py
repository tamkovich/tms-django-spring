from articles.models import Article
from django import forms
from django.forms import ModelForm


class ArticleCreateForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
    author_name = forms.CharField(max_length=50)
    rating = forms.IntegerField()
    topic = forms.CharField(max_length=50, required=False)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'topic', 'content', 'author_name', 'rating']

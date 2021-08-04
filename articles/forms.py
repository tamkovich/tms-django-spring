from django import forms


class ArticleCreateForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
    author_name = forms.CharField(max_length=50)
    rating = forms.IntegerField()
    topic = forms.CharField(max_length=50, required=False)

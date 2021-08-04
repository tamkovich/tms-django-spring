from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article
from articles.forms import ArticleCreateForm
from tms_django_lessons.forms import WriteLineForm


def index(request):
    print(request.GET)
    return HttpResponse("Hello world")


def home_page(request):
    if request.method == 'GET':
        form = WriteLineForm()
        return render(
            request,
            'home.html',
            context={"username": 'World', 'form': form},
        )
    elif request.method == 'POST':
        form = WriteLineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('Valid data:', data)
        else:
            print('Invalid data', form.errors)
        return render(
            request,
            'home.html',
            context={"username": form.data.username, 'form': form},
        )


def get_article_page(request):
    return render(
        request,
        'article.html',
    )


def add_article(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            Article.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author_name=form.cleaned_data['author_name'],
                rating=form.cleaned_data['rating'],
                topic=form.cleaned_data.get('topic'),
            )
    else:
        form = ArticleCreateForm()
    return render(
        request,
        'add_article.html',
        context={'form': form}
    )

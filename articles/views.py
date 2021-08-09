from articles.forms import ArticleCreateForm, ArticleForm
from articles.models import Article
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    print(request.GET)
    return HttpResponse("Hello world")


def home_page(request):
    articles = Article.objects.all()
    return render(
        request,
        'home.html',
        context={"articles": articles},
    )


def get_article_page(request):
    articles = Article.objects.all()

    return render(
        request,
        'article.html',
        context={"articles": articles},
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
            return redirect('home-page')
    else:
        form = ArticleCreateForm()
    return render(
        request,
        'add_article.html',
        context={'form': form}
    )


def article_edit(request, articles_id):
    article = get_object_or_404(Article, id=articles_id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        return render(request, 'article_edit.html', {'article': article, 'form': form})
    else:
        form = ArticleForm(request.POST, instance=article)
        form.save()
        return redirect('home-page')


def delete_article(request, articles_id):
    article = get_object_or_404(Article, id=articles_id)
    if request.method == 'POST':
        article.delete()
        return redirect('home-page')

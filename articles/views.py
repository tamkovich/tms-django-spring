from django.http import HttpResponse
from django.shortcuts import render

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


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print(request.GET)
    return HttpResponse("Hello world")


def home_page(request):
    return render(
        request,
        'index.html',
        context={"username": request.POST.get('username', 'World')},
    )

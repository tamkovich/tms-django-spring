
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = (r"<p>"
                r"<a href='/hw1901/'>Homework 19_01</a> <br> <br>"
                r"<a href='/hw1902/'>Homework 19_02</a> <br> <br>"
                r"<a href='/order/'>Homework 20</a>"
                r"</p>")
    return HttpResponse(response)


def home_page(request):
    name = request.POST.get("username", 'World')
    return render(request,
                  'index.html',
                  context={"username": 'World' if name == '' else name})

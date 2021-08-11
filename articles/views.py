from django.http import HttpResponse
from django.shortcuts import render
from tms_django_lessons.forms import AviaSales
import datetime


def index(request):
    print(request.GET)
    return HttpResponse("Hello World")


def home(request):
    if not request.POST.get("username"):
        return render(request,
                      'home.html',
                      context={"username": "world"})
    else:
        return render(request,
                  'home.html',
                  context={"username": request.POST.get("username", "world")})


def fun_HW19_01(request):
    max_length = max(str(request.POST.get("text1")), str(request.POST.get("text2")), str(request.POST.get("text2")), str(request.POST.get("text3")))
    return render(request,
                  'HW19_01.html',
                  context={"longest": max_length})


def fun_HW19_02(request):
    if not request.POST.get("calendar"):
        return render(request,
                      'HW19_02.html',
                      context={"longest": "Выберите дату"})
    else:
        data = str(request.POST.get("calendar"))
        list_of_data = data.split('-')
        print(list_of_data[2])
        if list_of_data[2] == "01":
            data1 = "C Новым "
            data2 = " годом"
            data_ = data1 + list_of_data[0] + data2
            return render(request,
                      'HW19_02.html',
                      context={"longest": data_})
        else:
            return render(request,
                          'HW19_02.html',
                          context={"longest": data})


def avia_page(request):
    if request.method == 'GET':
        form = AviaSales()
        return render(request, 'HW20.html',
                      context={"username": "world", "form": form})
    if request.method == 'POST':
        form = AviaSales(request.POST)
        if form.is_valid():
            return render(request, 'HW20.html',
                          context={'form': form, 'cost': form.cleaned_data['amountPerson'] * 100})
        else:
            print("Invalid data", form.errors)

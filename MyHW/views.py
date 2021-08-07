from django.shortcuts import render
from tms_django_lessons.forms import AviaSales
from datetime import datetime


def hw1901(request):
    messages = {request.POST.get('message01', ''):len(request.POST.get('message01', '')),
                request.POST.get('message02', ''):len(request.POST.get('message02', '')),
                request.POST.get('message03', ''):len(request.POST.get('message03', ''))}
    keymax = max(messages, key=messages.get)
    return render(request, 'HW_1901.html', context={'result':keymax})

def hw1902(request):
    if request.method == 'GET':
        date = request.POST.get('date', '')
        return render(request, 'HW_1902.html', context={'date': date})
    elif request.method == 'POST':
        date, format = request.POST.get('date', ''), '%Y-%m-%d'
        date = datetime.strptime(date, format)
        if date.month == 1 and date.day == 1:
            date = f'С новым {date.year} годом!'
            return render(request, 'HW_1902.html', context={'date': date})
        else:
            return render(request, 'HW_1902.html', context={'date':date.strftime('%Y-%m-%d')})

def additionaltask1(request):
    req = request.POST.get('username', 'World')
    if req == '':
        req = 'World'
    return render(request,
                  'additional_task1.html',
                  context={"username": f'{req}'})

def HW20(request):
    if request.method == 'GET':
        form = AviaSales()
        return render(request, 'HW_20.html',
                      context={'AviaSales': form})
    elif request.method == 'POST':
        form = AviaSales(request.POST)
        if form.is_valid():
            return render(request, 'HW_20.html',
                          context={'AviaSales': form, 'cost': form.cleaned_data['amountPerson'] * 100})
        else:
            print('Invalid data:', form.errors)

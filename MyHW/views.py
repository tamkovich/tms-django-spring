from django.shortcuts import render

def hw1901(request):
    messages = {request.POST.get('message01', ''):len(request.POST.get('message01', '')),
                request.POST.get('message02', ''):len(request.POST.get('message02', '')),
                request.POST.get('message03', ''):len(request.POST.get('message03', ''))}
    keymax = max(messages, key=messages.get)
    return render(request, 'HW_1901.html', context={'result':keymax})

def hw1902(request):
    date = request.POST.get('date', '')
    if date[5:7] == '01' and date[8:] == '01':
        date = f'С новым {date[0:4]} годом!'
    return render(request, 'HW_1902.html', context={'date':date})

def additionaltask1(request):
    req = request.POST.get('username', 'World')
    if req == '':
        req = 'World'
    return render(request,
                  'additional_task1.html',
                  context={"username": req})

from django.shortcuts import render

from tms_django_lessons.forms import WriteLineForm


def index(request):
    return render(request, 'index.html')


def articles(request):
    if request.method == 'GET':
        form = WriteLineForm()
        return render(request, 'articles.html', context={'username':'World', 'form':form},)
    elif request.method == 'POST':
        form = WriteLineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('Valid data:', data)
        else:
            print('Valid data:', form.errors)
        return render(request, 'articles.html',
                      context={'username':form.data.get('firstname'), 'form':form},)
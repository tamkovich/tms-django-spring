from django.shortcuts import render
from .models import InputLetters
from .forms import InputLettersForm


def home(request):
    error = ""
    if request.method == "POST":
        form = InputLettersForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('ready_timetable')
        else:
            error = "Пожалуйста, введите буквы."
    form = InputLettersForm()
    info = InputLetters.objects.all()
    return render(request, 'home.html', {"form": form, "error": error, "info": info})

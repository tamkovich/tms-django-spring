from datetime import datetime
from django.shortcuts import render


def start_page(request):
    """Ф-ция выводит стартовую страницу приложения"""
    return render(request, 'start_page.html')


def hw19_1(request):
    """Ф-ция выводит максимальное/ые по длине знач. поля из формы на странице."""
    if request.method == 'POST':
        w1 = str(request.POST.get('word1'))
        w2 = str(request.POST.get('word2'))
        w3 = str(request.POST.get('word3'))
        max_len = max(len(w1), len(w2), len(w3))
        list_word_max_len = []
        if max_len == 0:
            word_max_len = "Все поля пусты!"
        else:
            for i in (w1, w2, w3):
                if len(i) == max_len:
                    list_word_max_len.append(i)
            word_max_len = ", ".join(list_word_max_len)
        return render(request, 'HW-19-1.html', context={"maxlen": word_max_len})
    else:
        return render(request, 'HW-19-1.html', context={"maxlen": ""})


def hw19_2(request):
    """Ф-ция выводит поздравление с НГ или введенную дату в формате: г-м-д."""
    if request.method == 'POST':
        if request.POST.get('my_date'):
            date = datetime.strptime(request.POST.get('my_date'), "%Y-%m-%d")
            if date.day == 1 and date.month == 1:
                output_inf = f"С новым {date.year} годом."
            else:
                output_inf = f"Дата: {datetime.strftime(date, '%Y-%m-%d')}"
        else:
            output_inf = "Дата не заполнена!"
        return render(request, 'HW-19-2.html', context={"date_inf": output_inf})
    else:
        return render(request, 'HW-19-2.html', context={"date_inf": ""})

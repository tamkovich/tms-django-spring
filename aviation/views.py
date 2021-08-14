from aviation.forms import AviationCreateForm
from django.shortcuts import render


def hw20(request):
    """Ф-ция валидирует и обрабатывает данные формы, расчитывает стоимость"""
    total_cost = ""
    if request.method == 'POST':
        fly_form = AviationCreateForm(request.POST)
        if fly_form.is_valid():
            quantity = fly_form.cleaned_data['Сколько_человек']
            if quantity == "1":
                total_cost = "100$"
            else:
                total_cost = f"{100 * 2 * int(quantity)}$"
        else:
            total_cost = f"Данные не валидны! {fly_form.errors}"
    else:
        fly_form = AviationCreateForm()
    return render(
        request,
        'HW-20.html',
        context={'form': fly_form, 'cost': total_cost}
    )
# Денис, все работает, но в последнем return PyCharm выделяет HW-20.html
# с комментарием "Template file 'HW-20.html' not found".
# Все урлы настроены, переходы по ссылкам работают, чего ему не хватает?

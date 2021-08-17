from django.http import HttpResponse
from django.shortcuts import render, redirect

from HW21.models import Users
from HW21.forms import UserCreateForm


def start_page(request):
    """Ф-ция выводит стартовую страницу с краткой инф. о пользователях"""
    users = Users.objects.all()
    return render(request, 'start_page.html', context={"users": users})


def new_user(request):
    """Ф-ция валилирует данные формы и добавляет нового пользователя в DB."""
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            Users.objects.create(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                age=form.cleaned_data['age'],
                profession=form.cleaned_data['profession'],
            )
            return redirect('name-start-page')
        else:
            return HttpResponse(f'errors in {form.errors}')
    else:
        form = UserCreateForm()
        return render(request, 'new_user.html', context={'form': form})


def user_page(request):
    """Ф-ция выводит данные пользователя, позволяет удалить и изменить их."""
    user_id = request.GET.get("id")
    user = Users.objects.get(id=user_id)
    form2 = UserCreateForm(user.__dict__)
    mess = ""
    if request.POST.get('delete_user'):
        user.delete()
        mess = "Запись удалена, вернитесь на главную страницу!"
# хотел redirect на главную страницу, но в return нужно вернуть форму, поэтому через mess.
    if request.POST.get('update_user'):
        form3 = UserCreateForm(request.POST)
        if form3.is_valid():
            user.firstname = form3.cleaned_data['firstname']
            user.lastname = form3.cleaned_data['lastname']
            user.age = form3.cleaned_data['age']
            user.profession = form3.cleaned_data['profession']
            user.save()
            mess = "Запись обновлена, вернитесь на главную страницу!"
        else:
            mess = "Запись НЕ обновлена, данные не валидны!"
    return render(request, 'user_page.html', context={'form2': form2, 'mess': mess})
# буду благодарен за предложения по оптимизации моего решения (сам я им доволен :) ).

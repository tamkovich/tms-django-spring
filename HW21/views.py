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
    firstname = user.firstname
    lastname = user.lastname
    age = user.age
    profession = user.profession
    mess = ""
    if request.POST.get('delete_user'):
        user.delete()
        mess = "Запись удалена, вернитесь на главную страницу!"
# хотел redirect на главную страницу, но во 2-ом return
# есть context параметры, без них тут все ломается.
    if request.POST.get('update_user'):
        user.firstname = str(request.POST.get('fn'))
        user.lastname = str(request.POST.get('ln'))
        user.age = str(request.POST.get('ag'))
        user.profession = str(request.POST.get('prof'))
        user.save()
# user.update(.....) почему-то не работало, не находило метод update, хотя с delete() было ОК.
        mess = "Запись обновлена, вернитесь на главную страницу!"
    return render(
        request,
        'user_page.html',
        context={'id': user_id, 'firstname': firstname, 'lastname': lastname,
                 'age': age, 'profession': profession, 'mess': mess})
# ? не могу понять, почему в html при отображении profession теряется второе слово?
# ? возможно есть способ решения с заполнением значениями из DB именно формы,
#    но я такой ненагуглил (может ты что подскажешь), поэтому пока так.
# + буду благодарен за оценку оптимальности моего решения этой задачи.

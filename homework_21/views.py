from django.shortcuts import render
from faker import Faker
from random import randint
from homework_21.models import Users
from homework_21.forms import UserEditForm
from django.shortcuts import redirect


def fill_db(request):
    need_clear = request.GET.get('clr') == 'True'
    cnt = int(request.GET.get('cnt'))
    if need_clear:
        for user in Users.objects.filter():
            user.delete()

    fake = Faker()
    for _ in range(cnt):
        user = Users(firstname=fake.first_name(),
                     lastname=fake.last_name(),
                     age=randint(1, 122),
                     profession=fake.job())
        user.save()
    return redirect('users')


def show_users(request):
    if request.method == 'GET':
        user_id = request.GET.get('id', '')
        if user_id == '':
            all_users = Users.objects.filter()
            return render(request,
                          'users.html',
                          context={'all_users': all_users})
        else:
            user = Users.objects.filter(id=user_id)
            form = UserEditForm(initial=user.values()[0])
            # form = UserEditForm(initial={'firstname': user.first().firstname,
            #                              'lastname': user.first().lastname,
            #                              'age': user.first().age,
            #                              'profession': user.first().profession})
            return render(request,
                          'user-edit-form.html',
                          context={'form': form, 'user_id': f'ID: {user_id}'})
    elif request.method == 'POST':
        user_id = request.GET.get('id')
        if request.POST.get('Save'):
            form = UserEditForm(request.POST)
            if form.is_valid():
                user = Users.objects.get(id=user_id)
                user.firstname = form.cleaned_data['firstname']
                user.lastname = form.cleaned_data['lastname']
                user.age = form.cleaned_data['age']
                user.profession = form.cleaned_data['profession']
                user.save()
                return redirect('users')
            else:
                message = 'Wrong input. Please, check.'
                return render(request,
                              'user-edit-form.html',
                              context={'form': form,
                                       'user_id': f'ID: {user_id}',
                                       'message': message})
        elif request.POST.get('Delete'):
            user = Users.objects.get(id=user_id)
            user.delete()
            return redirect('users')


def add_user(request):
    if request.method == 'GET':
        form = UserEditForm()
        return render(request,
                      'user-add-form.html',
                      context={'form': form})
    elif request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            user = Users(firstname=form.cleaned_data['firstname'],
                         lastname=form.cleaned_data['lastname'],
                         age=form.cleaned_data['age'],
                         profession=form.cleaned_data['profession'])
            user.save()
            return redirect('users')
        else:
            message = 'Wrong input. Please, check.'
            return render(request,
                          'user-add-form.html',
                          context={'form': form,
                                   'message': message})

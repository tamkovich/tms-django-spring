from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserCreateForm, UserUpdateForm


def get_request_id(request):
    var = str(request)
    word_list = var.split("/")
    return [int(num) for num in filter(lambda num: num.isnumeric(), word_list)][0]

def users_list(request):
    users_list = CustomUser.objects.all()
    return render(request, "users/list.html", {"users_list": users_list})

def select_user(request):
    user_id_from_request = get_request_id(request)
    selected_user = CustomUser.objects.get(id=user_id_from_request)
    return render(request, "users/selected_user.html", {"selected_user": selected_user})

def create_user(request):
    error = ""
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
        else:
            error = "Смотри что пишешь!!!"
    form = UserCreateForm()
    return render(request, "users/create.html", {"form": form, "error": error})

def delete_user(request):
    user_id_from_request = get_request_id(request)
    customer = CustomUser.objects.get(id=user_id_from_request)
    customer.delete()
    return redirect('/users/')

def update_user(request):
    error = ""
    user_id_from_request = get_request_id(request)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            customer = CustomUser.objects.get(id=user_id_from_request)
            customer.firstname = form.cleaned_data['firstname']
            customer.lastname = form.cleaned_data['lastname']
            customer.age = int(form.cleaned_data['age'])
            customer.profession = form.cleaned_data['profession']
            customer.save()
            return redirect('/users/')
        else:
            error = "Смотри что пишешь!!!"
    form = UserUpdateForm()
    return render(request, 'users/update.html', {'form': form})


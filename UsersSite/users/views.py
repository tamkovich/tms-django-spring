from django.shortcuts import render
from users.models import CustomUser


def users_list(request):
    users_list = CustomUser.objects.all()
    return render(request, "users/list.html", {"users_list": users_list})

def select_user(request):
    var = str(request)
    word_list = var.split("/")
    user_id_from_request = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)][0]
    selected_user = CustomUser.objects.get(id=user_id_from_request)
    return render(request, "users/selected_user.html", {"selected_user": selected_user})
from MyHW.models import User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


class UserHome(ListView):
    model = User
    template_name = 'home.html'

class DetailViewclass(DetailView):
    model = User
    template_name = 'DetailUsersInfo.html'
    context_object_name = 'user'

class CreateViewclass(CreateView):
    model = User
    template_name = 'createuser.html'
    fields = ['firstname', 'lastname', 'age', 'profession']

class UpdateViewclass(UpdateView):
    model = User
    template_name = 'updateuser.html'
    fields = ['firstname', 'lastname', 'age', 'profession']

class DeleteViewclass(DeleteView):
    model = User
    template_name = 'deleteuser.html'
    success_url = '/'

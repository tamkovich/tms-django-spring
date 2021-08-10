from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^list_users/\d+/', views.select_user),
    url(r'^newuser/', views.create_user),
    url(r'^deluser/\d+/', views.delete_user),
    url(r'^updateuser/\d+/', views.update_user),
    url(r'^$', views.users_list),
]
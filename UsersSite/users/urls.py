from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^list_users/\d+/', views.select_user),
    url(r'^$', views.users_list),
]
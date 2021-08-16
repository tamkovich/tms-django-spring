from django.contrib import admin
from django.urls import path

from HW21.views import start_page, user_page, new_user

urlpatterns = [
    path('', start_page, name='name-start-page'),
    path('user-page/', user_page, name='name_user_page'),
    path('new-user/', new_user, name='name_new_users'),
    path('admin/', admin.site.urls),
]

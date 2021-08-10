from django.urls import path
from MyHW.views import DetailViewclass, UserHome, UpdateViewclass, DeleteViewclass, CreateViewclass

urlpatterns = [
    path('', UserHome.as_view(), name='UserHome'),
    path('create/', CreateViewclass.as_view(), name='CreateViewclass'),
    path('detailinfo/<int:pk>', DetailViewclass.as_view(), name='DetailViewclass'),
    path('updateuser/<int:pk>', UpdateViewclass.as_view(), name='UpdateViewclass'),
    path('deleteuser/<int:pk>', DeleteViewclass.as_view(), name='DeleteViewclass'),
]

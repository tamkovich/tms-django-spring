from django.urls import path

from aviation.views import hw20

urlpatterns = [
    path('HW20/', hw20, name='nameHW20'),
]

from django.urls import path

from .views import order_tikets

urlpatterns = [
    path('', order_tikets),
]
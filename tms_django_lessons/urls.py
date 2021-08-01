"""tms_django_lessons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from articles.views import index
from MyHW.views import hw1901, hw1902, additionaltask1

urlpatterns = [
    path('', index, name='index'),
    path('HW1901/', hw1901, name='hw1901'),
    path('HW1902/', hw1902, name='hw1902'),
    path('additionaltask/', additionaltask1, name='additionaltask1'),
    path('admin/', admin.site.urls),
]

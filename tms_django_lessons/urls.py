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

from articles.views import index, home, fun_HW19_01, fun_HW19_02, avia_page


urlpatterns = [
    path('', index),
    path('HW20/', avia_page, name="HW20-page"),
    path('HW1902/', fun_HW19_02, name="HW1902-page"),
    path('HW1901/', fun_HW19_01, name="HW1901-page"),
    path('home/', home),
    path('admin/', admin.site.urls),
]

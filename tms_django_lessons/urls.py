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

from articles.views import index, home_page, get_article_page, add_article, \
    article_edit, delete_article

urlpatterns = [
    path('', index),
    path('add-article/', add_article, name='add-article'),
    path('admin/', admin.site.urls),
    path('article/', get_article_page, name='article-page'),
    path('article-edit/', article_edit, name='article-edit'),
    path('article-edit/<int:articles_id>/', article_edit, name='article_edit'),
    path('article-edit/<int:articles_id>/delete', delete_article, name='delete_article'),
    path('home/', home_page, name='home-page'),
]

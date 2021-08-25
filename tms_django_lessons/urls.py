from django.contrib import admin
from django.urls import path, include

from articles.views import index, home_page, get_article_page, add_article

api_urlpatterns = [
    path('snippets/', include('snippets.urls')),
    path('users/', include('users.urls'))
]

urlpatterns = [
    path('', index),
    path('add-article/', add_article),
    path('article/', get_article_page),
    path('home/', home_page, name='home-page'),
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

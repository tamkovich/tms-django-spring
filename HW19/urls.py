from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from HW19.views import start_page, hw19_1, hw19_2

urlpatterns = [
    path('', start_page, name='name-start-page'),
    path('HW19-1/', hw19_1, name='nameHW19-1'),
    path('HW19-2/', hw19_2, name='nameHW19-2'),
    path('admin/', admin.site.urls),
    path('aviation/', include('aviation.urls')),
    path('HW20/', RedirectView.as_view(url='/aviation/', permanent=True)),
]

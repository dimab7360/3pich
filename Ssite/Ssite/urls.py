from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Ssite import settings
from Threepich.views import *
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Threepich.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




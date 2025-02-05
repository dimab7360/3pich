from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('osel', osel, name='osel'),
    path('about', about, name='about'),
]
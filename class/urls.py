from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    #APP
    path('app_checkimg', views.app_checkimg),
]
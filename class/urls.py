from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    #APP
    path('app_enter_room', views.app_enterroom),
    path('app_attendance', views.app_attendance),
    path('app_checkimg', views.app_checkimg),

]
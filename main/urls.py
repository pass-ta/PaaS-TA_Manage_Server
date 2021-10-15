from django.urls import path

from . import views


urlpatterns = [




    #APP
    path('app_login', views.app_login),
    path('app_signup', views.app_signup),
]
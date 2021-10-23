from django.urls import path

from . import views


urlpatterns = [




    #APP
    path('app_login', views.app_login),
    path('app_signup', views.app_signup),
    path('app_profileimg', views.app_profileimg),
    path('app_getprofileimg', views.app_getprofileimg),
]
from django.urls import path

from . import views


urlpatterns = [
    path('', views.main),
    path('login/', views.login),
    path('logout/', views.logout),


    #APP
    path('app_login', views.app_login),
    path('app_signup', views.app_signup),
    path('app_profileimg', views.app_profileimg),
    path('app_getprofileimg', views.app_getprofileimg),
]
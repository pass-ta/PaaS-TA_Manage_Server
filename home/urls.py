from django.urls import path

from . import views

# 기본 경로 = home/
urlpatterns = [
    path('', views.home),
    path('makeclass/',views.makeclass),
    path('makeclass/success', views.make_success),
]
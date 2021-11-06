from django.urls import path

from . import views

# 기본 경로 = home/
urlpatterns = [
    path('', views.home),
    path('makeclass/',views.makeclass),
    path('makeclass/success', views.make_success),

    path('enterclass/', views.enterclass),
    path('enterclass/teacher',views.teacher),
    path('enterclass/student1',views.student1),
    path('enterclass/student2',views.student2, name='student2'),
    path('enterclass/student3',views.student3),

       #APP
    path('app_enter_room', views.app_enterroom),
    path('app_attendance', views.app_attendance),
    path('app_checkimg', views.app_checkimg),
    path('app_sendcount', views.app_sendcount),
]
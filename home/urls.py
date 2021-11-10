from django.urls import path
from home.views import ClassList_t

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

    path('myclass/teacher',ClassList_t.as_view()),
    path('myclass/teacher/<int:pk>',views.classDetail),    # 공지사항
    path('myclass/teacher/quiz',views.classDetail2),       # 퀴즈
    path('myclass/teacher/analytics',views.classDetail3),  # 통계 자료


       #APP
    path('app_enter_room', views.app_enterroom),
    path('app_attendance', views.app_attendance),
    path('app_checkimg', views.app_checkimg),
    path('app_sendcount', views.app_sendcount),
]
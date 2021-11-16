from django.urls import path
from home.views import ClassList_s, ClassList_t

from . import views

# 기본 경로 = home/
urlpatterns = [
    path('', views.home),
    path('makeclass/',views.makeclass),
    path('makeclass/success', views.make_success),

    path('enterclass/', views.enterclass),
    path('class/makequiz',views.make_quiz),        # 퀴즈 만들기 
    path('enterclass/teacher',views.teacher),    # 버튼 누르면 webrtc 입장
    path('enterclass/student1',views.student1),
    path('enterclass/student2',views.student2, name='student2'),
    path('enterclass/studentquiz',views.student_quiz),
    path('enterclass/student3',views.student3),

    path('myclass/teacher',ClassList_t.as_view()),         # 선생님 calss list
    path('myclass/teacher/<int:pk>',views.classDetail_t),    # 공지사항
    path('myclass/teacher/<int:pk>/<int:pkk>',views.classDetail_Detail_t),    # 공지사항 세부 페이지
    path('myclass/teacher/<int:pk>/makenotice',views.makeNotice),    # 공지사항 만들기
    path('myclass/teacher/quiz',views.classDetail2_t),       # 퀴즈
    path('myclass/teacher/quiz/<int:pk>',views.classDetail2_Detail2_t),       # 퀴즈 상세보기
    path('myclass/teacher/analytics',views.classDetail3_t),  # 통계 자료
    path('myclass/teacher/analytics/<int:pk>',views.analyticsDetail),

    path('myclass/student',ClassList_s.as_view()),         # 학생 calss list
    path('myclass/student/<int:pk>',views.classDetail_s),    # 공지사항
    path('myclass/student/<int:pk>/<int:pkk>',views.classDetail_Detail_s),    # 공지사항 세부 페이지
    path('myclass/student/quiz',views.classDetail2_s),       # 퀴즈
    path('myclass/student/analytics',views.classDetail3_s),  # 통계 자료
    path('myclass/student/analytics/<int:pk>',views.analyticsDetail),

    path('classout/teacher', views.classOut_t),
    path('classout/student', views.classOut_s),
    path('classout/student/teacherquiz', views.teacher_quiz),       # 유림 퀴즈 푸는 url
    path('classout/student/analytics/<int:quiz>', views.analytics),  # 한식 통계자료 url

       #APP
    path('app_enter_room', views.app_enterroom),
    path('app_attendance', views.app_attendance),
    path('app_checkimg', views.app_checkimg),
    path('app_sendcount', views.app_sendcount),
]
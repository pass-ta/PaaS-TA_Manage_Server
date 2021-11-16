from django.contrib import admin
from .models import Room, Analytics, Enrol, Notice,SolvedQuiz
from .models import Room
from .models import Quiz
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_password', 'room_name',
                    'file', 'maker', 'make_date', 'member_list')


admin.site.register(Room, RoomAdmin)

class EnrolAdmin(admin.ModelAdmin):
    list_display =('email','room_id','room_password','room_name','make_date')

admin.site.register(Enrol, EnrolAdmin)

class AnalyticsAdmin(admin.ModelAdmin):
    list_display =('room_id','email','username','level','app','person','quiz','list','make_date')

admin.site.register(Analytics, AnalyticsAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display =('room_id','writer','writername','title','description','make_date')

admin.site.register(Notice, NoticeAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'maker','makername', 'room_id', 'question',
                    'item1', 'item2', 'item3', 'item4', 'answer','make_date')

admin.site.register(Quiz, QuizAdmin)

class SolvedQuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','makername', 'room_id', 'question',
                    'item1', 'item2', 'item3', 'item4', 'answer','make_date')

admin.site.register(SolvedQuiz, SolvedQuizAdmin)
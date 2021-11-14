from django.contrib import admin
from .models import Room
from .models import Quiz
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_password', 'room_name',
                    'file', 'maker', 'make_date', 'member_list')


admin.site.register(Room, RoomAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'maker', 'room_id', 'question',
                    'item1', 'item2', 'item3', 'item4', 'answer')


admin.site.register(Quiz, QuizAdmin)

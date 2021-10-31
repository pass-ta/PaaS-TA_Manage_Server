from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display =('room_id','room_password','room_name','file','maker','make_date','member_list')

admin.site.register(Room, RoomAdmin)

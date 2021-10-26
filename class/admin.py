from django.contrib import admin
from .models import Room
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display =('class_name','class_password','teacher','make_date','student_list')

admin.site.register(Room, ClassAdmin)


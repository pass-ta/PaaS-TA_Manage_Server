from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =('email','password','username','image','role','check','registerd_date')

admin.site.register(User, UserAdmin)
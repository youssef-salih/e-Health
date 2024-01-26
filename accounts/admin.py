from django.contrib import admin
from .models import *


# Register your models here.

class UserAdminSite(admin.ModelAdmin):
    model = User
    fields = ['first_name', 'last_name', 'email', 'role','is_active','phone_number','password' ]
    list_display = ('first_name', 'last_name', 'email', 'role','is_active')


admin.site.register(User,UserAdminSite)

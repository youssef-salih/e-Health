from django.contrib import admin
from .models import *


class DoctorAdminSite(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'start_time', 'end_time')


class RdvAdminSite(admin.ModelAdmin):
    list_display = ('full_name', 'doctor', 'phone_number', 'date', 'time')


admin.site.register(Doctor, DoctorAdminSite)
admin.site.register(TakeAppointment, RdvAdminSite)

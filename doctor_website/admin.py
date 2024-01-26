from django.contrib import admin

# Register your models here.
from doctor_website.models import Website, Service



class serviceAdminSite(admin.ModelAdmin):
    list_display = ('title', 'caption')


admin.site.register(Website)
admin.site.register(Service, serviceAdminSite)

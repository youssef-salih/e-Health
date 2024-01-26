"""
doctor_appointment_system URL Configuration

"""

from django.urls import path
from doctor_website.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'doctor_website'
urlpatterns = [
                  path('services', ServiceView.as_view(), name='service'),
                  path('doctors', DoctorView.as_view(), name='doctor'),
                  path('<pk>/doctors/active', DoctorActiveView.as_view(), name='doctoractive'),
                  path('service/create', AddServiceView.as_view(), name='add_service'),
                  path('<pk>/service/delete', ServiceDeleteView.as_view(), name='delete-service'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

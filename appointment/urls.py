"""
doctor_appointment_system URL Configuration

"""

from django.urls import path
from appointment.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appointment'
urlpatterns = [
                  path('', HomePageView.as_view(), name='home'),
                  path('doctor/appointment/create', AppointmentCreateView.as_view(), name='doctor-appointment-create'),
                  path('doctor/appointment/', AppointmentListView.as_view(), name='doctor-appointment'),
                  path('<pk>/delete/', AppointmentdoctorDeleteView.as_view(), name='delete-doctor-appointment'),
                  path('MyAppointement/', MyAppointement.as_view(), name='my-appointement'),
                  path('<pk>/appointement/delete', AppointmentDeleteView.as_view(), name='delete-appointment'),
                  path('patient-take-appointment/', TakeAppointmentView.as_view(), name='take-appointment'),
                  path('patient/', PatientListView.as_view(), name='patient-list'),
                  path('<pk>/patient/detail', DetailPatientView.as_view(), name='detail-patient'),
                  path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

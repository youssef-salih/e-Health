from django.urls import path
from .views import *
from appointment.views import *
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('patient/register', RegisterPatientView.as_view(), name='patient-register'),
    path('patient/profile/update/', EditPatientProfileView.as_view(), name='patient-profile-update'),
    path('doctor/register', RegisterDoctorView.as_view(), name='doctor-register'),
    path('doctor/profile/update/', EditDoctorProfileView.as_view(), name='doctor-profile-update'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

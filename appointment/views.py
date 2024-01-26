from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.models import User
from doctor_website.models import Website
from .decorators import user_is_patient, user_is_doctor
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from accounts.forms import PatientProfileUpdateForm, DoctorProfileUpdateForm
from .forms import TakeAppointmentForm, CreateAppointmentForm, detailappointementUpdateForm

from .models import Doctor, TakeAppointment

"""
For Patient Profile
    
"""


class EditPatientProfileView(UpdateView):
    model = User
    form_class = PatientProfileUpdateForm
    context_object_name = 'patient'
    template_name = 'accounts/patient/edit-profile.html'
    success_url = reverse_lazy('accounts:patient-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_patient)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Patient doesn't exists")
        return obj


class AppointmentdoctorDeleteView(DeleteView):
    """
       For Delete any Appointement created by Doctor
    """
    model = Doctor
    success_url = reverse_lazy('appointment:doctor-appointment')


class AppointmentCreateView(CreateView):
    template_name = 'appointment/appointment_create.html'
    form_class = CreateAppointmentForm
    extra_context = {
        'title': 'Post New Appointment'
    }
    success_url = reverse_lazy('appointment:doctor-appointment')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'doctor':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TakeAppointmentView(CreateView):
    template_name = 'appointment/take_appointment.html'
    form_class = TakeAppointmentForm
    extra_context = {
        'title': 'Take Doctor'
    }
    success_url = reverse_lazy('appointment:my-appointement')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'patient':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TakeAppointmentView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            messages.success(request, 'Appointement successfully')
            return self.form_valid(form)
        else:
            messages.info(request, 'appointement not successfully')
            return self.form_invalid(form)


class EditDoctorProfileView(UpdateView):
    model = User
    form_class = DoctorProfileUpdateForm
    context_object_name = 'doctor'
    template_name = 'accounts/doctor/edit-profile.html'
    success_url = reverse_lazy('accounts:doctor-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_doctor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Patient doesn't exists")
        return obj


class AppointmentListView(ListView):
    model = Doctor
    template_name = 'appointment/appointment.html'
    context_object_name = 'appointment'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_doctor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by('-id')


class PatientListView(ListView):
    model = TakeAppointment
    context_object_name = 'patients'
    template_name = "appointment/patient_list.html"

    def get_queryset(self):
        return self.model.objects.filter(doctor__user_id=self.request.user.id).order_by('date')


class DetailPatientView(UpdateView):
    model = TakeAppointment
    form_class = detailappointementUpdateForm
    context_object_name = 'app'
    template_name = 'appointment/details.html'
    success_url = reverse_lazy('appointment:patient-list')


class PatientDeleteView(DeleteView):
    model = TakeAppointment
    success_url = reverse_lazy('appointment:patient-list')


class AppointmentDeleteView(DeleteView):
    """
       For Delete any Appointement created by Patient
    """
    model = TakeAppointment
    success_url = reverse_lazy('appointment:my-appointement')


class HomePageView(ListView):
    model = Doctor
    context_object_name = 'home'
    template_name = "home.html"

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        doctor = Doctor.objects.all().order_by('-id')
        website = Website.objects.all()
        context = {
            'doc': doctor,
            'web': website
        }
        return context


class MyAppointement(ListView):
    model = TakeAppointment
    context_object_name = 'rdv'
    template_name = 'appointment/my_appointement.html'

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by('-id')

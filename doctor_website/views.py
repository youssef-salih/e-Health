from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.models import User
from doctor_website.forms import AddServiceForm, ActiveForm
from doctor_website.models import Service
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class ServiceView(ListView):
    model = Service
    context_object_name = 'serve'
    template_name = 'appointment/service.html'

    def get_queryset(self):
        return self.model.objects.all()


class AddServiceView(CreateView):
    template_name = 'appointment/service_create.html'
    form_class = AddServiceForm
    extra_context = {
        'title': 'Post New Service'
    }
    success_url = reverse_lazy('doctor_website:service')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddServiceView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ServiceDeleteView(DeleteView):
    """
       For Delete any Service created by admin
    """
    model = Service
    success_url = reverse_lazy('doctor_website:service')


class DoctorView(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'appointment/doctors.html'

    def get_queryset(self):
        return self.model.objects.filter(role='doctor')


class DoctorActiveView(UpdateView):
    model = User
    form_class = ActiveForm
    context_object_name = 'user'
    template_name = 'appointment/doctor.html'
    success_url = reverse_lazy('doctor_website:doctor')

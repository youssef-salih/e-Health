from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from accounts.forms import *
from accounts.models import User


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    wrong_url = '/services'
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_wrong_url(self):
        return self.wrong_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        if not self.request.user.is_active:
            auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
        Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterPatientView(CreateView):
    """
        Provides the ability to register as a Patient.
    """
    model = User
    form_class = PatientRegistrationForm
    template_name = 'accounts/patient/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request, 'patient registred successfully')
            return redirect('accounts:login')
        else:
            messages.info(request, 'patient not registred ')
            return render(request, 'accounts/patient/register.html', {'form': form})


class RegisterDoctorView(CreateView):
    """
       Provides the ability to register as a Doctor.
    """
    model = User
    form_class = DoctorRegistrationForm
    template_name = 'accounts/doctor/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request, 'doctors registred successfully')
            return redirect('accounts:login')
        else:
            messages.info(request, 'doctor not registred ')
            return render(request, 'accounts/doctor/register.html', {'form': form})

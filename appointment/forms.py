from datetime import datetime

from django import forms
from django.forms import DateInput

from .models import Doctor, TakeAppointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Full Name"
        self.fields['image'].label = "Image"
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )
        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex : 9 AM',
            }
        )
        self.fields['end_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 5 PM',
            }
        )

    class Meta:
        model = Doctor
        fields = ['full_name', 'image', 'start_time', 'end_time']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class TakeAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TakeAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].label = "Choose Your Doctor"
        self.fields['full_name'].label = "Full Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['date'].label = "date"
        self.fields['time'].label = "time"
        self.fields['allergie'].label = "Allergie"

        self.fields['doctor'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Doctor',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['allergie'].widget.attrs.update(
            {
                'placeholder': 'Write a short allergie',
            }
        )
        self.fields['analyse'].widget.attrs.update(
            {
                'multiple': True
            }
        )

    class Meta:
        model = TakeAppointment
        widgets = {'date': DateInput(), 'time': TimeInput}
        fields = ['doctor', 'full_name', 'phone_number', 'allergie', 'analyse', 'date', 'time']

    def is_valid(self):
        valid = super(TakeAppointmentForm, self).is_valid()
        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class detailappointementUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detailappointementUpdateForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )
        self.fields['allergie'].widget.attrs.update(
            {
                'readonly': 'readonly'

            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'readonly': 'readonly'

            }
        )

    class Meta:
        model = TakeAppointment
        fields = ["full_name", "allergie", "phone_number", "date", "time", "status"]
        widgets = {'date': DateInput(), 'time': TimeInput}

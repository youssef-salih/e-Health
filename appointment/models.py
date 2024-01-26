from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import User

status_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('canceled', 'Canceled'))


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploadedimages/doctorimage',null=True)
    start_time = models.CharField(max_length=10,null=True)
    end_time = models.CharField(max_length=10,null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name


class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    allergie = models.TextField(default="none")
    phone_number = models.CharField(max_length=10)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status = models.CharField(max_length=15, choices=status_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    analyse = models.FileField(upload_to='uploadedimages/analyse', null=True, blank=True)

    def __str__(self):
        return self.full_name

# Generated by Django 4.1 on 2022-08-26 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('start_time', models.CharField(max_length=10, null=True)),
                ('end_time', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakeAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('allergie', models.TextField(default='none')),
                ('phone_number', models.CharField(max_length=120)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('analyse', models.FileField(blank=True, null=True, upload_to='uploadedimages/analyse')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

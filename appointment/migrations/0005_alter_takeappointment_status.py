# Generated by Django 4.1 on 2022-08-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_takeappointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takeappointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=15),
        ),
    ]

# Generated by Django 4.1 on 2022-08-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_alter_takeappointment_analyse'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeappointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='Pending', max_length=15),
        ),
    ]

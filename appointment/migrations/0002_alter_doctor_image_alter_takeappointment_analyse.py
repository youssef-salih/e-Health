# Generated by Django 4.1 on 2022-08-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploadedimages/doctorimage'),
        ),
        migrations.AlterField(
            model_name='takeappointment',
            name='analyse',
            field=models.ImageField(blank=True, null=True, upload_to='uploadedimages/analyse'),
        ),
    ]
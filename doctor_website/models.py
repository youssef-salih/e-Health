from django.db import models


# Create your models here
class Website(models.Model):
    images = models.ImageField(upload_to='uploadedimages/website')
    slogang = models.CharField(max_length=500)

    def __str__(self):
        return self.slogang


class Service(models.Model):
    caption = models.CharField(max_length=500)
    title = models.CharField(max_length=40)
    image_icon = models.ImageField(upload_to='uploadedimages/service')

    def __str__(self):
        return self.title

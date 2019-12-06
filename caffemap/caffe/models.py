from django.db import models
from profile.models import Profile

class Caffe(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    user = models.ManyToManyField(Profile)
    logo = models.CharField(max_length=30)
    class Meta:
            ordering = ('name',)

    def __str__(self):
        return self.name    


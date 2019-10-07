from django.db import models
# from user.models import Profile

class Caffe(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    # user = models.ManyToManyField(Profile)



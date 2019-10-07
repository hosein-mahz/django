from django.db import models
# from caffe.models import Caffe

class Profile(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    # brandname = models.CharField(Caffe)

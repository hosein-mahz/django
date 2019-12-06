from django.db import models
from profile.models import Profile
from django.conf import settings


class Caffe(models.Model):
    brand      = models.CharField(max_length=30)
    name       = models.CharField(max_length=30)
    address    = models.CharField(max_length=30)
    user       = models.ManyToManyField(Profile)
    logo       = models.ImageField(upload_to='Caffe')
    location_x = models.CharField(max_length=50)
    location_y = models.CharField(max_length=50)
    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name    

CAFFEFILE_CHOISE = [
    (1, 'Image'),
    (2, '3D'),
    (3, 'panaroma'),
]
class Caffefile(models.Model):
    Caffe_id = models.ForeignKey(Caffe, null =True ,on_delete  =True)
    category = models.IntegerField(choices=CAFFEFILE_CHOISE, , null=True )
    # file= models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)

DESK_CHOISE = [
    (1, 'Suitable for work'),
    (2, 'Suitable for romantic dating'),
    (3, 'Suitable for birth'),
    (3, 'meeting'),
]
class Desk(models.Model):
    Caffe_id = models.ForeignKey(Caffe, null =True ,on_delete  =True)
    category = models.IntegerField(choices=DESK_CHOISE, , null=True )
    desk_name= models.CharField(max_length=200)

class Staff(models.Model):
    name           = models.CharField(max_length=200)
    position       =models.CharField(max_length=200)
    certification  = models.CharField(max_length=200)
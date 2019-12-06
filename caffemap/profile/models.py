from django.db import models

    class Profile(models.Model):
    name                         = models.CharField(max_length=30)
    lastname                     = models.CharField(max_length=30)
    username                     = models.CharField(max_length=10)
    password                     = models.CharField(max_length=30)
    email                        = models.CharField(max_length=120)
    phone                        = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + ' ' + self.lastname


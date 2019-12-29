from django.db import models
from caffe.models import Caffe   

# MENU_CHOISE = [
#     (1, 'Hot drink'),
#     (2, 'cold drink'),
#     (3, 'Hookah'),
#     (4, 'Traditional food'),
#     (5, 'fast food'),
#     (6, 'Cake'),
#     (7, 'Appetizer'),
# ]


class Menu(models.Model):
    Caffe_id = models.ForeignKey(Caffe, null=True ,on_delete =True)
    # gender = models.IntegerField(choices=PATIENT_CHOISE,)

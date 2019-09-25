from django.contrib import admin
from user.models import Profile
from caffe.models import Caffe

admin.site.register(Profile)
admin.site.register(Caffe)

# from django.contrib import admin
# from django.db.models import get_models, get_app

# for model in get_models(get_app('bama')):
#     admin.site.register(model)
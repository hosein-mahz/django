from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

# from django.contrib import admin
# from django.db.models import get_models, get_app

# for model in get_models(get_app('bama')):
#     admin.site.register(model)
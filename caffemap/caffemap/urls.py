from django.contrib import admin
from django.urls import path
from caffe import views as view_caffe
from profile import views as view_profile
from menu import views as view_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/', view_caffe.dev),

    # 
    # C A F F E
    # 
    path('caffe/', view_caffe.getAll),
    path('caffe/get/<int:__id>', view_caffe.getSingle),
    path('caffe/create/', view_caffe.create),
    path('caffe/delete/<int:_id>', view_caffe.delete),
    path('caffe/update/<int:_id>', view_caffe.update),

    # 
    # P R O F I L E
    # 
    path('profile/', view_profile.getAll),
    path('profile/dev/', view_profile.dev),
    path('profile/get/<int:id>', view_profile.getSingle),
    # path('profile/',view_profile.getAll),
    # path('profile/create/', view_profile.create),
    # path('profile/delete/<int:_id>',view_profile.delete),
    # path('profile/update/<int:_id>', view_profile.update),

    # 
    # M E N U
    # 
    # path('menu/',view_menu.getAll)
]




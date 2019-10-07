from django.contrib import admin
from django.urls import path
from caffe import views as view_caffe
from user import views as view_user
from meno import views as view_meno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getall/', view_caffe.getAll),
    path('dev/', view_caffe.dev),
    path('caffe/get/<int:__id>', view_caffe.getSingle),
    path('caffe/create/', view_caffe.create),
    path('caffe/delete/<int:_id>', view_caffe.delete),
    path('caffe/update/<int:_id>', view_caffe.update),
    path('user/devv/', view_user.dev),
    path('user/get/<int:id>', view_user.getSingle),
    # path('user/',view_user.getAll),
    # path('user/create/', view_user.create),
    # path('user/delete/<int:_id>',view_user.delete),
    # path('user/update/<int:_id>', view_user.update),
    path('meno/',view_meno.getAll)
]




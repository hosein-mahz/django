from django.contrib                 import admin
from django.urls                    import include, path
from rest_framework                 import routers
from profile                        import views as view_profile
# from caffe import views as view_caffe
# from menu import views as view_menu

from caffe.viewses.views           import caffeViewSet
from caffe.viewses.viewsCaffefile  import CaffefileViewSet
from caffe.viewses.viewsdesk       import DeskViewSet
from caffe.viewses.viewsStaff      import StaffViewSet

from profile.views                 import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'caffe'     , caffeViewSet)
router.register(r'Caffefile' , CaffefileViewSet)
router.register(r'Desk'      , DeskViewSet)
router.register(r'Staff'     , StaffViewSet)

router.register(r'Profile'     , ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    

]

    # path('dev/', view_caffe.dev),

    # 
    # P R O F I L E
    # # 
    # path('profile/', view_profile.getAll),
    # path('profile/dev/', view_profile.dev),
    # path('profile/get/<int:_id>', view_profile.getSingle),
    # path('profile/create/', view_profile.create),
    # path('profile/delete/<int:_id>', view_profile.delete),
    # path('profile/update/<int:_id>', view_profile.update),
    # # 
    # # C A F F E
    # # 
    # path('caffe/', view_caffe.getAll),
    # path('caffe/get/<int:__id>', view_caffe.getSingle),
    # path('caffe/create/', view_caffe.create),
    # path('caffe/delete/<int:_id>', view_caffe.delete),
    # path('caffe/update/<int:_id>', view_caffe.update),


    # # 
    # # M E N U
    # # 
    # # path('menu/',view_menu.getAll)



from rest_framework import serializers
from caffe.models import Caffe, Caffefile, Desk, Staff
# from profile.models import Profile  

class CaffeSerializer(serializers.ModelSerializer):
    desk        = serializers.StringRelatedField(many=True)
    Caffefile   = serializers.StringRelatedField(many=True)
    class Meta:
        model = Caffe
        fields = [
            'brand',
            'name',
            'address',
            'logo',
            'location_x',
            'location_y',
            'user',
            'id',
            'Caffefile',
            'desk'
        ]


class CaffefileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caffefile
        fields = [
            'Caffe_id',
            'category',
            'id'
            # 'file'
        ]

class DeskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Desk
        fields = [
            'Caffe_id',
            'category',
            'desk_name',
            'id'
        ]

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = [
            'name',
            'position',
            'certification',
            'id'
        ]

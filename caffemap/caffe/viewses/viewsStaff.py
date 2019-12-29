from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from caffe.models import Staff
from rest_framework import viewsets
from caffe.serializers import StaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('-name')
    serializer_class = StaffSerializer
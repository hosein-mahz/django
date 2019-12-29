from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from caffe.models import Caffe
from caffe.models import Caffefile
from rest_framework import viewsets
from caffe.serializers import CaffefileSerializer

class CaffefileViewSet(viewsets.ModelViewSet):
    queryset = Caffefile.objects.all().order_by('-category')
    serializer_class = CaffefileSerializer
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from caffe.models import Caffe
from caffe.models import Desk
from rest_framework import viewsets
from caffe.serializers import DeskSerializer

class DeskViewSet(viewsets.ModelViewSet):
    queryset = Desk.objects.all().order_by('-desk_name')
    serializer_class = DeskSerializer
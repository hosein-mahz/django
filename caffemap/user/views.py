from django.http import HttpResponse , JsonResponse
from django.core import serializers
from .models import Profile
from caffe.models import Caffe
from json import loads

def getAll(request):
    g = serializers.serialize("json", Profile.objects.all())
    data = loads(g)
    result = []
    for x in data:
        e = x['fields']['user']
        # e = loads(serializers.serialize("json", [Caffe.objects.get(id=e)]))
        x['fields']['id']=x['pk']
        x['fields']['user']=e[0]
        result.append(x['fields'])
    return JsonResponse(result, safe=False)

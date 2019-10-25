from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Profile
from caffe.models import Caffe
from json import loads

def dev(request):
    g = serializers.serialize("json", Profile.objects.all())
    data = loads(g) 
    return JsonResponse(data, safe=False)

def getAll(request):
    # 
    # with database model
    # 
    g = serializers.serialize("json", Profile.objects.all())
    data = loads(g)
    o = []
    for x in data:
        x['fields']['id']=x['pk']
        for y in x['fields']['caffe']:
            a = loads(serializers.serialize("json", [Caffe.objects.get(id=y)]))
            o.append(a[0]['fields'])
        x['fields']['caffe']=o
        o = []
        # x['fields'].append(o)
        # 
        # FIXME:
        # 
        # Profile.objects.get(id=1).caffe_set.all()
        # 
    return JsonResponse(data, safe=False)

def getSingle(request, __id):
    g = serializers.serialize("json",[Profile.objects.get(id=__id)])
    data = loads(g)
    data[0]['fields']['id']=data[0]['pk']
    return JsonResponse(data[0]['fields'], safe=False)

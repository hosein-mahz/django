from django.http import HttpResponse , JsonResponse
from django.core import serializers
from user.models import Profile
from caffe.models import Caffe
from json import loads

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
    return JsonResponse(data, safe=False)




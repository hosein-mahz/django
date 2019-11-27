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
    for x in data:
        x['fields']['id']=x['pk']
        l = serializers.serialize("json", Profile.objects.get(pk=x['pk']).caffe_set.all() )
        l = loads(l)
        x['fields']['caffe'] = []
        for y in l:
            x['fields']['caffe'].append(y['fields'])
        
    return JsonResponse(data, safe=False)

def getSingle(request, __id):
    g = serializers.serialize("json",[Profile.objects.get(id=__id)])
    data = loads(g)
    data[0]['fields']['id']=data[0]['pk']
    return JsonResponse(data[0]['fields'], safe=False)

def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['name'] == '' or hasattr(data, 'name') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
            _Profile = Profile(name = data['name'], lastname = data['lastname'], username = data['username'], password = data['password'], email = data['email'])
            _Profile.save()
            return JsonResponse({'message':'successful create new Profile'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)

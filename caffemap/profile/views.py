from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Profile
from caffe.models import Caffe
from json import loads
from .models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer

def convertToJson(_QuerySet):
    g = serializers.serialize("json", _QuerySet)
    _data = loads(g) 
    return _data

def dev(request):
    data = convertToJson(Profile.objects.all())
    return JsonResponse(data, safe=False)

# 
#  Helper Methods
#  
def helperId(_object):
    _object['fields']['id']=_object['pk']
    return _object

# ///////////////////////////////////////
def getAll(request):
    data = convertToJson(Profile.objects.all())
    for x in data:
        l = convertToJson( Profile.objects.get(pk=x['pk']).caffe_set.all() )
        l = helperId(l)
        x['fields']['caffe'] = []
        for y in l:
            x['fields']['caffe'].append(y['fields'])
        
    return JsonResponse(data, safe=False)

def getSingle(request, _id):
    data = convertToJson( Profile.objects.get(id=_id) )
    data[0] = helperId(data[0])
    return JsonResponse(data[0]['fields'], safe=False)

def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['name'] == '' or hasattr(data, 'name') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
            _Profile = Profile(
                name = data['name'],
                lastname = data['lastname'],
                username = data['username'],
                password = data['password'],
                email = data['email'])
            _Profile.save()
            return JsonResponse({'message':'successful create new Profile'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)

def delete(request, _id): 
    if request.method == 'DELETE':
        try:
            Profile.objects.filter(pk=_id).delete()
            return JsonResponse({'message': 'successfull deleting'}, safe=False)
        except:
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
    return JsonResponse({'message': 'most use DELETE method'}, safe=False)

def update(request, _id):
    if request.method == 'PUT':
        try:
            data = loads(request.body)
            Profile.objects.filter(id=_id).update(
                name=data['name'],
                lastname=data['lastname'],
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            return JsonResponse({'message': 'successfull updating'}, safe=False)
        except : 
            return JsonResponse({'message': 'unsuccessfull updating'}, safe=False)
# ///////////////////////////////////////

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-name')
    serializer_class = ProfileSerializer
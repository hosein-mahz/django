from django.http import HttpResponse , JsonResponse
from django.core import serializers
from profile.models import Profile
from json import loads
from caffe.models import Caffe
from rest_framework import viewsets
from caffe.serializers import CaffeSerializer


# //////////////////////////////////////////////////
def dev(request):
    g = serializers.serialize("json", Caffe.objects.all())
    data = loads(g) 
    return JsonResponse(data, safe=False)

def getAll(request):
    # 
    # with database model
    # 
    g = serializers.serialize("json", Caffe.objects.all())
    data = loads(g)
    o = []
    for x in data:
        x['fields']['id']=x['pk']
        for y in x['fields']['user']:
            a = loads(serializers.serialize("json", [Profile.objects.get(id=y)]))
            o.append(a[0]['fields'])
        x['fields']['user']=o
        o = []
        # x['fields'].append(o)
    return JsonResponse(data, safe=False)

def getSingle(request, __id):
    g = serializers.serialize("json",[Caffe.objects.get(id=__id)])
    data = loads(g)
    data[0]['fields']['id']=data[0]['pk']
    return JsonResponse(data[0]['fields'], safe=False)

def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['brand'] == '' or hasattr(data, 'brand') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
            _caffe = Caffe(brand = data['brand'], name = data['name'], address = data['address'])
            _caffe.save()
            return JsonResponse({'message':'successful create new caffe'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)

def delete(request, _id): 
    if request.method == 'DELETE':
        try:
            Caffe.objects.filter(id=_id).delete()
            return JsonResponse({'message': 'successfull deleting'}, safe=False)
        except:
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
    return JsonResponse({'message': 'most use DELETE method'}, safe=False)

def update(request, _id):
    if request.method == 'PUT':
        try:
            data = loads(request.body)
            Caffe.objects.filter(id=_id).update(
                brnd=data['brnd'],
                company=data['company'],
                volume=data['volume']
            )
            return JsonResponse({'message': 'successfull updating'}, safe=False)
        except : 
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
# ///////////////////////////////////////////////////////////

class caffeViewSet(viewsets.ModelViewSet):
    queryset = Caffe.objects.all().order_by('-name')
    serializer_class = CaffeSerializer
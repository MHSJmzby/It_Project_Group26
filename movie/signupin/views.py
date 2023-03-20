from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
import json
from common.models import User
from common.MyEncoder import MyEncoder

# Create your views here.
def signup(request):
    print(request.body)
    request.params = json.loads(request.body)
    info=request.params
    print(info)
    record=User.objects.create(
        username=info['name'],
        password=info['password'],
        email=info['email'],
        state=0,
    )
    return JsonResponse({'code':'0','id':record.id})

def signin(request):
    info = json.loads(request.body)
    user=User.objects.filter(username=info['name'], password=info['password'],state=info['state'])
    if(len(user)==0):
        return JsonResponse({
            'code':'1',
            'msg':'Login Failure'
        })
    user=serializers.serialize("json",user)
    return JsonResponse({'code':'0','data':user})

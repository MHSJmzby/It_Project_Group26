from django.http import JsonResponse
from django.shortcuts import render
from common.models import Film
import json
# Create your views here.
def dispatcher(request):
    if request.method == 'GET':
        return moviemanagement(request)
    elif request.method == 'POST':
        return movieEdit(request)

def moviemanagement(request):
    name = request.GET['search']
    if (len(name) == 0):
        films = Film.objects.values()
    else:
        films = Film.objects.filter(filmName=name)
    films = list(films)
    return JsonResponse({'code': '0', 'data': films})

def movieEdit(request):
    print(request.body)
    info=json.loads(request.body)
    record=Film.objects.create(name=info['movie'],
                               screen=info['position'],
                               releaseTime=info['releaseDate'],
                               downTime=info['downDate'],
                               timeLength=info['duration'],
                               price=info['price'],
                               actor=info['actor'],
                               introduction=info['introduction'])
    return JsonResponse({'code':'0'})
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from common.models import Film,ScheduleFilm
import json
# Create your views here.
def dispatcherMovie(request):
    if request.method == 'GET':
        return moviemanagement(request)
    elif request.method == 'PUT':
        return movieEdit(request)
    elif request.method == 'POST':
        return movieAdd(request)

def dispatcherschedule(request):
    if request.method == 'GET':
        return schedule(request)
    elif request.method == 'PUT':
        return scheduleEdit(request)

def moviemanagement(request):
    name = request.GET['search']
    print(name)
    if (len(name) == 0):
        films = Film.objects.values()
        films = list(films)
    else:
        films = Film.objects.filter(name=name)
        films = serializers.serialize('json', films)
    return JsonResponse({'code': '0', 'data': films})

def movieAdd(request):
    print(request.body)
    info=json.loads(request.body)
    record=Film.objects.create(name=info['name'],
                               screen=info['screen'],
                               releaseTime=info['releaseTime'],
                               downTime=info['downTime'],
                               timeLength=info['timeLength'],
                               price=info['price'],
                               actor=info['actor'],
                               introduction=info['introduction'],
                               state=info['state'])
    return JsonResponse({'code':'0'})


def movieEdit(request):
    info = json.loads(request.body)
    record=Film.objects.get(id=info['id'])
    record.name=info['name']
    record.screen=info['screen']
    record.releaseTime=info['releaseTime']
    record.downTime=info['downTime']
    record.timeLength=info['timeLength']
    record.price=info['price']
    record.actor=info['actor']
    record.introduction=info['introduction']
    record.tate=info['state']
    record.save()
    return JsonResponse({'code':'0'})


def schedule(request):
    sche=ScheduleFilm.objects.values()
    sche=list(sche)
    return JsonResponse({'code':'0','data':sche})

def scheduleEdit(request):
    infos = json.loads(request.body)
    print(infos)
    for info in infos:
        record=ScheduleFilm.objects.get(id=info['id'])
        record.timing=info['timing']
        record.monday=info['monday']
        record.tuesday=info['tuesday']
        record.wednesday=info['wednesday']
        record.thursday=info['thursday']
        record.friday=info['friday']
        record.saturday=info['saturday']
        record.sunday=info['sunday']
        record.save()
    return JsonResponse({'code': '0'})
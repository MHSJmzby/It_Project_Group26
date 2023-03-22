import json
import datetime

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from common.models import Order, Film, User

ISOT = '%Y-%m-%d %H:%M:%S'

def dispatcherBooking(request):
    if request.method == 'GET':
        return booking(request)
    elif request.method == 'POST':
        return book(request)


def dispatcherHistoryOrder(request):
    if request.method == 'GET':
        return historyorder(request)

# Create your views here.
def historyorder(request):
    name=request.GET['search']
    userid=request.GET['userId']
    if(len(name)==0):
        orders=Order.objects.values()
        orders = list(orders)
    else:
        orders=Order.objects.filter(filmName=name,userId=userid)
        orders = list(orders)
        orders = serializers.serialize('json', orders)
    return JsonResponse({'code':'0','data':orders})


def refund(request):
    info = json.loads(request.body)
    order=Order.objects.get(id=info['id'])
    order.state=2
    order.save()
    return JsonResponse({'code':'0'})


def booking(request):
    name = request.GET['search']
    if (len(name) == 0):
        films = Film.objects.values()
        films = list(films)
    else:
        films = Film.objects.filter(name=name)
        films = serializers.serialize('json', films)
    return JsonResponse({'code': '0', 'data': films})


def book(request):
    info = json.loads(request.body)
    #print(info)

    user, movie = info.split(' ')
    str, userId = user.split(':')
    str, movieId = movie.split(':')
    # print(userId, movieId)

    film = Film.objects.get(id=movieId)
    record = Order.objects.create(
        userId=int(userId),
        filmName=film.name,
        time=datetime.datetime.now().strftime(ISOT),
        price=film.price,
        screen=film.screen,
        state=1,
    )
    return JsonResponse({'code':'0'})


def editUser(request):
    info=json.loads(request.body)
    print(info)
    record = User.objects.get(id=info['id'])
    record.username = info['username']
    record.password = info['password']
    record.email = info['email']
    record.vipValidDate = info['vipValidDate']
    record.state = info['state']
    record.save()
    user=User.objects.filter(id=info["id"])
    user = serializers.serialize("json", user)
    return JsonResponse({'code': '0','data':user})
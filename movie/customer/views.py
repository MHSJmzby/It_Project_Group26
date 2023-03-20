import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from common.models import Order, Film


def dispatcherBooking(request):
    if request.method == 'GET':
        return booking(request)
    elif request.method == 'POST':
        return book(request)


def dispatcherHistoryOrder(request):
    if request.method == 'GET':
        return historyorder(request)
    elif request.method == 'DELETE':
        return refund(request)

# Create your views here.
def historyorder(request):
    name=request.GET['search']
    if(len(name)==0):
        orders=Order.objects.values()
        orders = list(orders)
    else:
        orders=Order.objects.filter(filmName=name)
        orders = serializers.serialize('json', orders)
    return JsonResponse({'code':'0','data':orders})


def refund(request):
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
    print(info)
    return JsonResponse({'code':'0'})
from django.http import JsonResponse
from django.shortcuts import render
from common.models import Order
# Create your views here.
def historyorder(request):
    name=request.GET['search']
    if(len(name)==0):
        orders=Order.objects.values()
    else:
        orders=Order.objects.filter(filmName=name)
    orders=list(orders)
    return JsonResponse({'code':'0','data':orders})
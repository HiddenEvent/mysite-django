from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer


@csrf_exempt
def order_list(request, shopId):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shopId)
        return render(request, 'boss/order_list.html', {'order_list': order_list})

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        estimated_time = request.POST['estimated_time']
        order_item = Order.objects.get(pk=order_id)
        order_item.estimated_time = estimated_time
        order_item.save()
        shopId = order_item.shop.id
        return render(request, 'boss/success.html', {'shopId': shopId})
    else:
        return HttpResponse(status=404)

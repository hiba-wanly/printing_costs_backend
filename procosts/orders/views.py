from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict


# Create your views here.

@csrf_exempt
@api_view(["POST"])
def create(request):
    user_name = request.data.get('user_name')
    user_id = request.data.get('user_id')
    to_perosn = request.data.get('to_perosn')
    project = request.data.get('project')
    printer = request.data.get('printer')
    time = request.data.get('time')
    material = request.data.get('material')
    quantity = request.data.get('quantity')
    price_or_order = request.data.get('price_or_order')
    date = request.data.get('date')
    total_price = request.data.get('total_price')
    finance = request.data.get('finance')
    supervisor = request.data.get('supervisor')
    membership = request.data.get('membership')
    gain = request.data.get('gain')
    risk = request.data.get('risk')
    material_costs = request.data.get('material_costs')
    owner = request.data.get('owner')
    order = Orders.objects.create(
        user_name = user_name,
        user_id = user_id,
        to_perosn = to_perosn,
        project = project,
        printer = printer,
        time = time,
        material = material,
        quantity = quantity,
        price_or_order = price_or_order,
        date = date,
        total_price = total_price,
        finance = finance,
        supervisor = supervisor,
        membership = membership,
        gain = gain,
        risk = risk,
        material_costs = material_costs,
        owner = owner
    )
    data = model_to_dict(order)
    return Response({'status' : 200,'message' : 'order was added successfully','data' : data},status=200)

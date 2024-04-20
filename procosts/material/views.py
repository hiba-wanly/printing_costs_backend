from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict

# Create your views here.
@api_view(['GET'])
def getAll(request):
    material = list(Materials.objects.values())
    return Response({
       'status' : 200,
       'message' : 'Data retrieved  successfully',
       'data' : material
    },status=200)


@csrf_exempt
@api_view(["POST"])
def create(request):
    name = request.data.get('name')
    unit = request.data.get('unit')
    price = request.data.get('price')
    number_of_units = request.data.get('number_of_units')
    color = request.data.get('color')
    brand = request.data.get('brand')
    if not name or not unit or not price or not number_of_units or not color or not brand:
            return Response({'status' : 404,'massage' : ' can not be null' , 'data' :{}},status= 404)
    cost_per_One = int(price) / int(number_of_units)
    material = Materials.objects.create(name = name,unit = unit,price = price,number_of_units = number_of_units,cost_per_One = cost_per_One, color = color, brand = brand)
    data = model_to_dict(material)
    material2 = list(Materials.objects.values())
    return Response({'status' : 200,'message' : 'material was added successfully','data' : material2})


@csrf_exempt
@api_view(["POST"])
def update(request, id):
    try:
        data = Materials.objects.get(id = id)
        name = request.data.get('name')
        unit = request.data.get('unit')
        price = request.data.get('price')
        number_of_units = request.data.get('number_of_units')
        color = request.data.get('color')
        brand = request.data.get('brand')
        if not data:
            return Response({'status' : 404,'message' : 'cant not find data id','data' : {}},status=404)
        if name:
            data.name = name
        if unit:    
            data.unit = unit
        if price:
            data.price = price
            data.cost_per_One = int(data.price) / int(data.number_of_units)
        if number_of_units:
            data.number_of_units = number_of_units 
            data.cost_per_One = int(data.price) / int(data.number_of_units) 
        if color:
             data.color = color
        if brand:
             data.brand = brand           
        data.save()    
        material = model_to_dict(data)
        material2 = list(Materials.objects.values())
        return JsonResponse({'status' : 200,'message' : 'material was updated successfully','data' : material2})
    except Materials.DoesNotExist:
        return JsonResponse({'status' : 404,'message' : 'cant not find data','data' : {}})
     


@csrf_exempt
@api_view(["DELETE"])
def delete(request, id):
        data = Materials.objects.filter(id = id).first()
        if not data:
            return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)
        data.delete()
        material = list(Materials.objects.values())
        return JsonResponse({'status' : 200,'message' : 'material was deleted successfully','data' : material})
   



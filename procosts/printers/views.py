from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict

# Create your views here.
@api_view(['GET'])
def getAll(request):
    printer = list(Printers.objects.values())
    return Response({
       'status' : 200,
       'message' : 'Data retrieved  successfully',
       'data' : printer
    },status=200)


@csrf_exempt
@api_view(["POST"])
def create(request):
    name = request.data.get('name')
    preparation_cost = request.data.get('preparation_cost')
    start_up_cost = request.data.get('start_up_cost')
    printer_wear_and_tear = request.data.get('printer_wear_and_tear')
    depreciation_in_hours = request.data.get('depreciation_in_hours')
    inverter_and_battery_wear = request.data.get('inverter_and_battery_wear')
    kilowatts_old = request.data.get('kilowatts_old')
    electricity_courier = request.data.get('electricity_courier')
    single_material = request.data.get('single_material')
    termination_costs = request.data.get('termination_costs')
    supervision_costs = request.data.get('supervision_costs')

    if not name or not preparation_cost or not start_up_cost or not printer_wear_and_tear or not depreciation_in_hours or not inverter_and_battery_wear or not kilowatts_old or not electricity_courier or not single_material or not termination_costs or not supervision_costs:
        return Response({'status' : 404,'massage' : 'faild cannot be null' , 'data' :{}},status= 404)
    courier_depreciation = int(printer_wear_and_tear) / int(depreciation_in_hours)
    price_per_kilowatt_with_depreciation = (int(inverter_and_battery_wear)/int(kilowatts_old))+0.03
    electricity_costs = float(electricity_courier) * price_per_kilowatt_with_depreciation
    courier_printing = electricity_costs + courier_depreciation
    printer = Printers.objects.create(
        name = name,preparation_cost = preparation_cost, start_up_cost =start_up_cost,
        printer_wear_and_tear =printer_wear_and_tear,depreciation_in_hours =depreciation_in_hours,
        inverter_and_battery_wear = inverter_and_battery_wear, kilowatts_old=kilowatts_old,
        electricity_courier=electricity_courier,single_material=single_material,
        termination_costs=termination_costs,supervision_costs=supervision_costs,
        courier_depreciation=courier_depreciation,price_per_kilowatt_with_depreciation=price_per_kilowatt_with_depreciation,
        electricity_costs=electricity_costs,courier_printing=courier_printing
    )
    data = model_to_dict(printer)
    printer = list(Printers.objects.values())
    return Response({'status' : 200,'message' : 'printer was added successfully','data' : printer},status=200)

@csrf_exempt
@api_view(["POST"])
def update(request, id):
    try:
        data = Printers.objects.filter(id = id).first()
        name = request.data.get('name')
        preparation_cost = request.data.get('preparation_cost')
        start_up_cost = request.data.get('start_up_cost')
        printer_wear_and_tear = request.data.get('printer_wear_and_tear')
        depreciation_in_hours = request.data.get('depreciation_in_hours')
        inverter_and_battery_wear = request.data.get('inverter_and_battery_wear')
        kilowatts_old = request.data.get('kilowatts_old')
        electricity_courier = request.data.get('electricity_courier')
        single_material = request.data.get('single_material')
        termination_costs = request.data.get('termination_costs')
        supervision_costs = request.data.get('supervision_costs')
        if not data:
             return Response({'status' : 404,'message' : 'cant not find data ','data' : {}},status=404)
        if name:
             data.name = name
        if preparation_cost:
             data.preparation_cost=preparation_cost   
        if start_up_cost:
             data.start_up_cost =start_up_cost
        if printer_wear_and_tear:
             data.printer_wear_and_tear=printer_wear_and_tear
             data.courier_depreciation = int(data.printer_wear_and_tear) / int(depreciation_in_hours)
             data.courier_printing = data.electricity_costs + data.courier_depreciation 
        if depreciation_in_hours:
             data.depreciation_in_hours=depreciation_in_hours
             data.courier_depreciation = int(data.printer_wear_and_tear) / int(data.depreciation_in_hours)
             data.courier_printing = data.electricity_costs + data.courier_depreciation 
        if inverter_and_battery_wear:
             data.inverter_and_battery_wear=inverter_and_battery_wear
             data.price_per_kilowatt_with_depreciation = (int(data.inverter_and_battery_wear)/int(data.kilowatts_old))+0.03
             data.electricity_costs = float(data.electricity_courier) * data.price_per_kilowatt_with_depreciation
             data.courier_printing = data.electricity_costs + data.courier_depreciation 
        if kilowatts_old:
             data.kilowatts_old=kilowatts_old
             data.price_per_kilowatt_with_depreciation = (int(data.inverter_and_battery_wear)/int(data.kilowatts_old))+0.03
             data.electricity_costs = float(data.electricity_courier )* data.price_per_kilowatt_with_depreciation 
             data.courier_printing = data.electricity_costs + data.courier_depreciation 
        if electricity_courier:
             data.electricity_courier=electricity_courier 
             data.electricity_costs = float(data.electricity_courier) * data.price_per_kilowatt_with_depreciation  
             data.courier_printing = data.electricity_costs + data.courier_depreciation 
        if single_material:
             data.single_material=single_material
        if termination_costs:
             data.termination_costs=termination_costs
        if supervision_costs:
             data.supervision_costs=supervision_costs                                           
        data.save()
        printer = model_to_dict(data)
        printer2 = list(Printers.objects.values())
        return Response({'status' : 200,'message' : 'printer was updated successfully','data' : printer2},status=200)
    except Printers.DoesNotExist:
        return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)
     


@csrf_exempt
@api_view(["DELETE"])
def delete(request, id):
        data = Printers.objects.filter(id = id).first()
        if not data:
             return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)
        data.delete()
        printer = list(Printers.objects.values())
        return Response({'status' : 200,'message' : 'printer was deleted successfully','data' : printer},status=200)
        
   


from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from account.models import User

# Create your views here.
@api_view(['GET'])
def getAll(request):
    finance = list(Finance.objects.values())
    return Response({
       'status' : 200,
       'message' : 'Data retrieved  successfully',
       'data' : finance
    },status=200)

@csrf_exempt
@api_view(["POST"])
def create(request):
    coins = request.data.get('coins')
    if not coins:
            return Response({'status' : 404,'massage' : 'coins can not be null' , 'data' :{}},status= 404)
    coin = Finance.objects.create(coins = coins)
    data = model_to_dict(coin)
    return Response({'status' : 200,'message' : 'coins was added successfully','data' : data},status=200)

@csrf_exempt
@api_view(["POST"])
def update(request, id):
    try:
        data = Finance.objects.filter(id = id).first()
        coins = request.data.get('coins')
        if not data or not coins:
            return Response({'status' : 404,'message' : 'cant not find data or coins','data' : {}},status=404)
        data.coins = coins
        data.save() 
        coin = model_to_dict(data)
        finance = list(Finance.objects.values())
        return Response({'status' : 200,'message' : 'coins was updated successfully','data' :finance },status=200)
    except Finance.DoesNotExist:
        return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404) 

@csrf_exempt
@api_view(["DELETE"])
def delete(request, id):
       data = Finance.objects.filter(id = id).first()
       if not data:
           return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)
       data.delete()
       return Response({'status' : 200,'message' : 'coins was deleted successfully','data' : {} },status=200)
   
   

@csrf_exempt
@api_view(["POST"])  
def addORupdate(request ,pk):
     coins = request.data.get('coins')
     try:
          finance = Finance.objects.get(user_id = pk)
          if finance:
                finance.coins = coins
                finance.save()
                finance2 = Finance.objects.get(user_id = pk)
                finance2 = model_to_dict(finance2)
                return Response({'status' : 200,'message' : 'finance was updated successfully','data' : finance2},status=200)
          user = User.objects.get(id =pk)
          finance = Finance.objects.create( coins = coins, user_id = pk)
          finance2 = Finance.objects.get(user_id = pk)
          finance2 = model_to_dict(finance2)
          return Response({'status' : 200,'message' : 'finance was created2 successfully','data' : finance2},status=200)
     except Finance.DoesNotExist:
          print(1)
          user = User.objects.filter(id = pk).first()
          print(2)
          finance = Finance.objects.create( coins = coins, user_id = pk)
          finance2 = Finance.objects.get(user_id = pk)
          finance2 = model_to_dict(finance2)
          return Response({'status' : 200,'message' : 'finance was created successfully','data' : finance2},status=200)               

@api_view(['GET'])
def getUserFinance(request, pk):
    try:
        finance = Finance.objects.get(user_id = pk)
        finance2 = model_to_dict(finance)
        return Response({
           'status' : 200,
           'message' : 'Data retrieved  successfully',
           'data' : finance2
        },status=200)
    except Finance.DoesNotExist:
         return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)


   
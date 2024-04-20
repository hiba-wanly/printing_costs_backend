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
    other = list(Other.objects.values())
    return Response({
       'status' : 200,
       'message' : 'Data retrieved  successfully',
       'data' : other
    },status=200)


@csrf_exempt
@api_view(["POST"])
def create(request):
     gain = request.data.get('gain')
     risk = request.data.get('risk')
     if not gain or not risk :
         return Response({'status' : 404,'massage' : 'gain or risk cannot be null' , 'data' :{}},status= 404)
     other = Other.objects.create(gain = gain, risk = risk)
     data = model_to_dict(other)
     return Response({'status' : 200,'message' : 'other was added successfully','data' : data},status=200)

@csrf_exempt
@api_view(["POST"])
def update(request, id):
    try:
        data = Other.objects.filter(id = id).first()
        gain = request.data.get('gain')
        risk = request.data.get('risk')
        if gain:
            data.gain = gain
        if risk:    
            data.risk = risk
        data.save()    
        other = model_to_dict(data)
        other2 = list(Other.objects.values())
        return Response({'status' : 200,'message' : 'other was updated successfully','data' : other2},status=200)
    except Other.DoesNotExist:
        return Response({'status' : 404,'message' : 'cant not find data','data' : {}},status=404)
     


@csrf_exempt
@api_view(["DELETE"])
def delete(request, id):
        data = Other.objects.filter(id = id).first()
        if not data:
             return Response({'status' : 404,'message' : 'cantnot find data','data' : {}},status=404)
        data.delete()
        return Response({'status' : 200,'message' : 'other was deleted successfully','data' : {}},status=200)
        

@csrf_exempt
@api_view(["POST"])  
def addORupdate(request ,pk):
     gain = request.data.get('gain')
     risk = request.data.get('risk')
     try:
          other = Other.objects.get(user_id = pk)
          if other:
                other.risk = risk
                other.gain = gain
                other.save()
                other2 = Other.objects.get(user_id = pk)
                other2 = model_to_dict(other2)
                return Response({'status' : 200,'message' : 'other was updated successfully','data' : other2},status=200)
          user = User.objects.get(id =pk)
          other = Other.objects.create(gain = gain, risk = risk, user_id = pk)
          other2 = Other.objects.get(user_id = pk)
          other2 = model_to_dict(other2)
          return Response({'status' : 200,'message' : 'other was created2 successfully','data' : other2},status=200)
     except Other.DoesNotExist:
          print(1)
          user = User.objects.filter(id = pk).first()
          print(2)
          other = Other.objects.create(gain = gain, risk = risk, user_id = pk)
          other2 = Other.objects.get(user_id = pk)
          other2 = model_to_dict(other2)
          return Response({'status' : 200,'message' : 'other was created successfully','data' : other2},status=200)               


               
@api_view(['GET'])
def getUserOther(request, pk):
    other = Other.objects.get(user_id = pk)
    other2 = model_to_dict(other)
    return Response({
       'status' : 200,
       'message' : 'Data retrieved  successfully',
       'data' : other2
    },status=200)     


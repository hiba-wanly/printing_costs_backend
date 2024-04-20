from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import UserRegisterSerilaizer, LoginSerializer, LogoutSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Create your views here.
class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerilaizer

    def post(sefl, request):
        user_data = request.data
        serializer = sefl.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            # print(user)
            user1 = User.objects.get(email = user['email'])
            print(user1)
            refresh = RefreshToken.for_user(user1)
            print(refresh)
      
            return Response({
                'data':user,
                'message' : f'hi thanks for signing up a passcode',
                'refresh':str(refresh),
                'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        sreializer = self.serializer_class(data=request.data,context={'request':request})
        sreializer.is_valid(raise_exception=True)
        return Response({
            'data' :sreializer.data,
        },
            status=status.HTTP_200_OK)


class ChangePhotoView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self,request, id):
        try:
            user = User.objects.get(id = id)
            image = request.FILES.get('logo')
            if image:
                user.logo = image
                user.save()
                serializer = LoginSerializer(user)
                return Response({
                   'data' :{
                       'id': user.id,
                       'email': f'{user.email}',
                       'full_name':f'{ user.get_full_name}',
                       'logo': f'{user.logo}'
                       }
                },
                   status=status.HTTP_200_OK)
            return Response({
                   'data' :'add image ',
                },
                   status=status.HTTP_200_OK)

        except User.DoesNotExist:
             return Response({
                   'data' :'not found',
                },
                   status=status.HTTP_404_NOT_FOUND)
        

class LogoutUserView(GenericAPIView):
    serializer_class = LogoutSerializer  
    permission_classes = [IsAuthenticated]

    def post(self , request):
        serializer = self.serializer_class(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)  
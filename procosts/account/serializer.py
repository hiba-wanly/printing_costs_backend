from tokenize import TokenError
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken ,Token 
import hashlib

class UserRegisterSerilaizer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length = 6, write_only = True)


    class Meta:
        model = User
        fields = ['email','first_name','last_name','logo','password']

    def validate(self, attrs):
        password = attrs.get('password', '')
        return super().validate(attrs)

    def create(self, validated_data):
        # hash_pass = make_password(validated_data.get('password'))
        sha_signature = hashlib.sha256(validated_data.get('password').encode()).hexdigest()
        user = User.objects.create(
            email = validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            password = sha_signature,
        )
    
        return user 


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length =6)
    password = serializers.CharField(max_length=68,write_only= True)
    full_name=serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255,read_only=True)
    refresh_token = serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email','password','full_name','logo', 'access_token','refresh_token']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        # hash_pass = make_password(password)
        request = self.context.get('request')
        user= auth.authenticate(request,email = email,password=password)
        try:
             sha_signature = hashlib.sha256(password.encode()).hexdigest()
             user = User.objects.get(email = email,password =sha_signature)
     
             print(email)
             print(password)
            #  if not user:
                #  raise AuthenticationFailed("invalide credentials try again")
             # if not user.is_verified:
                 # raise AuthenticationFailed("Email is not verified")
             user_token = user.tokens()
             
             return {
                 'id' : user.id,
                 'email' : user.email,
                 'full_name' : user.get_full_name,
                 'logo' : user.logo,
                 'refresh_token' : str(user_token.get('refresh')),
                 'access_token' : str(user_token.get('access'))
             }    
        except User.DoesNotExist:
            raise AuthenticationFailed("invalide credentials try again")


class LogoutSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField()

    class Meta:
        model = User
        fields = ['refresh_token']

    default_error_messages ={
        'bad_token':('token is Invalid or has expired')
    }

    def validate(self, attrs):
        self.token = attrs.get('refresh_token')
        return attrs
    
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail    

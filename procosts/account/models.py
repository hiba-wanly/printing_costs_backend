from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to= 'logo/' , blank=True)

    USERNAME_FIELD ="email"

    REQUIRED_FIELDS = ["first_name","last_name"]

    objects =  UserManager()

    def __str__(self) :
        return self.email
    
    @property
    def get_full_name(self) :
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self) : 
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access': str(refresh.access_token)
        }

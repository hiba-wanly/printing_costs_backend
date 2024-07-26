from django.db import models
from account.models import User
# Create your models here.
class UserMaterials(models.Model):
    name = models.CharField(max_length = 250)
    unit = models.CharField(max_length = 250)
    price = models.IntegerField()
    number_of_units = models.IntegerField()
    cost_per_One = models.FloatField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    color = models.CharField(max_length = 250,null= True , blank=True)
    brand = models.CharField(max_length = 250,null= True , blank=True)
    owner = models.CharField(max_length = 250,null= True , blank=True,default="")


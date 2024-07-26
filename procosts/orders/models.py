from django.db import models
from account.models import User
# Create your models here.
class Orders(models.Model):
    user_name = models.CharField(max_length = 250)
    user_id = models.IntegerField()
    to_perosn = models.CharField(max_length = 250)
    project = models.CharField(max_length = 250)
    printer = models.CharField(max_length = 250)
    time = models.FloatField()
    material = models.CharField(max_length = 250)
    quantity =  models.FloatField()
    price_or_order = models.CharField(max_length = 250)
    date = models.CharField(max_length = 250)
    total_price =  models.FloatField() 
    finance = models.IntegerField()
    supervisor = models.CharField(max_length = 250)
    membership = models.CharField(max_length = 250)
    gain = models.IntegerField()
    risk = models.IntegerField()
    material_costs = models.FloatField(null= True , blank=True)
    owner = models.CharField(max_length = 250,null= True , blank=True)

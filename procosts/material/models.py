from django.db import models

# Create your models here.
class Materials(models.Model):
    name = models.CharField(max_length = 250)
    unit = models.CharField(max_length = 250)
    price = models.IntegerField()
    number_of_units = models.IntegerField()
    cost_per_One = models.FloatField()
    color = models.CharField(max_length = 250,null= True , blank=True)
    brand = models.CharField(max_length = 250,null= True , blank=True)
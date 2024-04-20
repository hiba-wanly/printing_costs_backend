from django.db import models
from account.models import User
# Create your models here.
class Other(models.Model):
    gain = models.IntegerField()
    risk = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

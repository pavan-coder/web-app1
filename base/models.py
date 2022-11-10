from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class tenant_Room(models.Model):
    Total_amount=models.IntegerField(null=False,blank=False)
    amount_per_head=models.IntegerField(null=False,blank=False)
    House_photos = models.ImageField(null = True)
    #max_members=
    address = models.TextField(null=False,blank=False)
    city = models.CharField( max_length=70,blank=False)
    state =models.CharField(max_length=70,blank=False)
    country = models.CharField(max_length=40,blank=False)
    updated = models.DateTimeField(auto_now =True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address 

class 

from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class tenant_Room(models.Model):
    tenant_name =models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.TextField(null=False,blank=False)
    city = models.CharField(_(""), max_length=50)
    updated = models.DateTimeField(auto_now =True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tenant 

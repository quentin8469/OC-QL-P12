from django.db import models
#from user.models import User
from user.models import TeamUser

# Create your models here.
# class Client(models.Model):
#     """ create model client"""
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=20)
#     company_name = models.CharField(max_length=250)
#     date_create = models.DateTimeField(auto_now_add=True)
#     date_update = models.DateTimeField(auto_now=True)
#     sales_contact = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True)
    
#     def __str__(self):
#         return f"{self.company_name}, {self.last_name}, {self.first_name}"
    
#     class Meta:
#         verbose_name = 'Client'
#         verbose_name_plural = 'Clients'
        

class Client(models.Model):
    """ create model client"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=TeamUser,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.company_name}, {self.last_name}, {self.first_name}"
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
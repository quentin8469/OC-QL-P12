from django.db import models
from django.conf import settings
from client.models import Client

# Create your models here.
class Contract(models.Model):
    """ Creat the contract objet"""
    
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    client = models.ForeignKey(to=Client,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField()
    
    def __str__(self):
        return f"{self.client}, {self.sales_contact}"
    
    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        ordering = ['status']
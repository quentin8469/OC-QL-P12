from django.db import models
from django.db.models.base import Model

# Create your models here.
class Team(models.Model):
    """ create model team to add a role to the user"""
    roles = [('sales', 'Sales'),
             ('management', 'Management'),
             ('support', 'Support')]
    
    role = models.CharField(max_length=100, choices=roles)
    

class User(models.Model):
    """Create the user model"""
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    #role = models.ForeignKey(to=Team)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
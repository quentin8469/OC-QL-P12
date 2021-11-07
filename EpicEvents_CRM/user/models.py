from _typeshed import Self
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Team(models.Model):
#     """ create model team to add a role to the user"""
#     roles_choices = [('sales', 'Sales'),
#              ('management', 'Management'),
#              ('support', 'Support')]
    
#     role = models.CharField(max_length=50, choices=roles_choices)
    

# class User(models.Model):
#     """Create the user model"""
    
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=50)
#     role = models.ForeignKey(to=Team,on_delete=models.CASCADE,null=True )
    
#     def __str__(self):
#         return f"{self.last_name}, {self.first_name}"
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


class TeamUser(models.Model):
    """ Create the team user model"""
    roles_choices = [('sales', 'Sales'),
                    ('management', 'Management'),
                    ('support', 'Support')
                    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=roles_choices)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.role}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    
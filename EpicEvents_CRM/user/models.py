from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Team(models.Model):
    """ create model team to add a role to the user"""
    roles_choices = [('sales', 'Sales'),
                     ('management', 'Management'),
                     ('support', 'Support')]
    
    role = models.CharField(max_length=50, choices=roles_choices)
    
    def __str__(self):
        return f"{self.role}"


class TeamUser(AbstractUser):
    """ Create the team user model  """
    
    role = models.ForeignKey(to=Team,on_delete=models.CASCADE,null=True )
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.role}"
    
    class Meta:
        verbose_name = 'Team User'
        verbose_name_plural = 'Teams Users'
        ordering = ['role']
        


from django.db import models
from user.models import TeamUser
from client.models import Client

# Create your models here.
class Event(models.Model):
    """ Create the Event object """
    
    client = models.ForeignKey(to=Client,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=TeamUser,on_delete=models.CASCADE,null=True)
    #event_status = 
    attendees = models.IntegerField()
    even_date = models.DateTimeField()
    notes = models.TextField()
    
    def __str__(self):
        return f"{self.client}, {self.support_contact}, {self.date_created}"
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['even_date']
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from .serializers import EventSerializer
from .models import Event
from client.models import Client
from contract.models import Contract


# Create your views here.

class EventViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Event.objects.all()
    
    def get_queryset(self):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        return Event.objects.filter(client=client)
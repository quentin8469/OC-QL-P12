from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from .permission import EventPermission

from .serializers import EventSerializer
from .models import Event
from client.models import Client
from contract.models import Contract
import logging


# Create your views here.
logger = logging.getLogger(__name__)

class EventViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
    #queryset = Event.objects.all()
    
    def get_queryset(self):
        user_team = self.request.user.role.role 
        if user_team == 'support':
            queryset = Event.objects.filter(support_contact=self.request.user)
        elif user_team == 'sales':
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            queryset = client.event_set.all()
        else:
            return Event.objects.all()
        
        client_name = self.request.query_params.get('client_name')
        client_email = self.request.query_params.get('email')
        event_date = self.request.query_params.get('date')
        
        if client_name is not None:
            queryset = queryset.filter(client__last_name=client_name)
        if client_email is not None:
            queryset = queryset.filter(client__email=client_email)
        if event_date is not None:
            queryset = queryset.filter(even_date=event_date)
        
        return queryset
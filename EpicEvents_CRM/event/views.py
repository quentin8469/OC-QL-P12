from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from .permission import EventPermission

from .serializers import EventSerializer
from .models import Event
from client.models import Client
from contract.models import Contract


# Create your views here.

class EventViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
    #queryset = Event.objects.all()
    
    def get_queryset(self):
        user_team = self.request.user.role.role 
        if user_team == 'support':
            return Event.objects.filter(support_contact=self.request.user)
        elif user_team == 'sales':
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            return client.event_set.all()
        else:
            return Event.objects.all()
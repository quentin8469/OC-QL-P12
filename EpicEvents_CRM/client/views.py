from rest_framework import viewsets, permissions
from django.http.response import Http404
from .serializers import ClientSerializer
from .models import Client
from event.models import Event
from .permission import ClientPermission
import logging


# Create your views here.
logger = logging.getLogger(__name__)


class ClientViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
    
    def get_queryset(self):
        user_team = self.request.user.role.role 
        if user_team == 'sales':
            queryset = Client.objects.filter(sales_contact=self.request.user)
        elif user_team == 'support':
            event = Event.objects.filter(support_contact=self.request.user)
            id_client = event.values_list('client', flat=True)
            queryset = Client.objects.filter(pk__in=id_client )
        else:
            return Client.objects.all()
        
        client_lastname = self.request.query_params.get('name')
        client_email = self.request.query_params.get('email')
        
        if client_lastname is not None:
            queryset = queryset.filter(last_name=client_lastname)
        if client_email is not None:
            queryset = queryset.filter(email=client_email)
        logger.warning('bob')     
        return queryset
        
    def perform_create(self, serializer):
        try:
            serializer.save(sales_contact=self.request.user)
        except:
            logger.info('bad')
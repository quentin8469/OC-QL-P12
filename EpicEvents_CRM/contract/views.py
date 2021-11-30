from django.http.response import Http404
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .serializers import ContractSerializer
from .models import Contract
from client.models import Client
from .permission import ContractPermission
import logging

# Create your views here.
logger = logging.getLogger(__name__)

class ContractViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]
    
    
    def get_queryset(self):
        user_team = self.request.user.role.role
        if user_team == 'sales':
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            queryset = client.contract_set.all().filter(sales_contact= self.request.user)
        else:
            return Contract.objects.all()
        
        client_name = self.request.query_params.get('client_name')
        client_email = self.request.query_params.get('email')
        contract_date = self.request.query_params.get('date')
        contract_amount = self.request.query_params.get('amount')
        
        if client_name is not None:
            queryset = queryset.filter(client__last_name=client_name)
        if client_email is not None:
            queryset = queryset.filter(client__email=client_email)
        if contract_date is not None:
            queryset = queryset.filter(date_create=contract_date)
        if contract_amount is not None:
            queryset = queryset.filter(amount=contract_amount)
        
        return queryset
        
    
    def perform_create(self, serializer):
        try:
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            serializer.save(sales_contact=self.request.user, client=client)
        except:
            logger.debug('not found')
        
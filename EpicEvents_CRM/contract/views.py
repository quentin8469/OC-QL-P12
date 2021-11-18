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
    #queryset = Contract.objects.all()
    
    def get_queryset(self):
        user_team = self.request.user.role.role
        if user_team == 'sales':
            client = get_object_or_404(Client, pk=self.kwargs['client_id'])
            return client.contract_set.all().filter(sales_contact= self.request.user)
        else:
            return Contract.objects.all()
    
    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(sales_contact=self.request.user, client=client)
        
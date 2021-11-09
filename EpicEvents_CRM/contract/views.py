from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .serializers import ContractSerializer
from .models import Contract
from client.models import Client


# Create your views here.

class ContractViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ContractSerializer
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Contract.objects.all()
    
    def get_queryset(self):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        
        return Contract.objects.filter(client=client )
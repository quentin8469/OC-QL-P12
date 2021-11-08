from rest_framework import viewsets, permissions
from .serializers import ContractSerializer
from .models import Contract


# Create your views here.

class ContractViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ContractSerializer
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Contract.objects.all()
    
    def get_queryset(self):
        return Contract.objects.all()
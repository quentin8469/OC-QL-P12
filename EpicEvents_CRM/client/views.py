from rest_framework import viewsets, permissions
from .serializers import ClientSerializer
from .models import Client


# Create your views here.

class ClientViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Client.objects.all()
    
    def get_queryset(self):
        return Client.objects.all()
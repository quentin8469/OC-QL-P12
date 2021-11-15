from rest_framework import viewsets, permissions
from .serializers import ClientSerializer
from .models import Client
from event.models import Event
from .permission import ClientPermission


# Create your views here.

class ClientViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
    
    def get_queryset(self):
        user_team = self.request.user.role.role 
        if user_team == 'sales':
            return Client.objects.filter(sales_contact=self.request.user)
        else:
            return Client.objects.all()
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
        elif user_team == 'support':
            event = Event.objects.filter(support_contact=self.request.user)
            id_client = event.values_list('client', flat=True)
            return Client.objects.filter(pk__in=id_client )
        else:
            return Client.objects.all()
        
    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)
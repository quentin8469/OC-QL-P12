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
        # elif user_team == 'support':
        #     events = Event.objects.filter(support_contact=self.request.user)
        #     print('bob1', events)# tout mes objet events du support
        #     for event in events:
        #         id_client_event = event['client']
        #         print('bob2', id_client_event)
        #         id_client = id_client_event.filter('pk')
        #         return Client.objects.filter(id_client)
        # elif user_team == 'support':
        #     id_client_event = Event.objects.
        #     return Client.objects.filter(pk=id_client_event )
        else:
            return Client.objects.all()
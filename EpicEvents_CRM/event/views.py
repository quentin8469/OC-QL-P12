from rest_framework import viewsets, permissions
from .serializers import EventSerializer
from .models import Event


# Create your views here.

class EventViewset(viewsets.ModelViewSet):
    """"""
    
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Event.objects.all()
    
    def get_queryset(self):
        return Event.objects.all()
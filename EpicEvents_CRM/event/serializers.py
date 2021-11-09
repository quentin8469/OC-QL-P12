from rest_framework import serializers
from .models import Event, EventStatus


class EventSerializer(serializers.ModelSerializer):
    """ Event serializer """
    class Meta:
        model = Event
        fields = "__all__"

        
class EventStatusSerializer(serializers.ModelSerializer):
    """ Event serializer """
    class Meta:
        model = EventStatus
        fields = "__all__"
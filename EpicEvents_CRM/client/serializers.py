from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelField):
    """ Client serializer """
    class Meta:
        model = Client
        fields = "__all__"
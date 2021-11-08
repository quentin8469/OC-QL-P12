from rest_framework import serializers
from .models import Contract


class ClientSerializer(serializers.ModelField):
    """ Client serializer """
    class Meta:
        model = Contract
        fields = "__all__"
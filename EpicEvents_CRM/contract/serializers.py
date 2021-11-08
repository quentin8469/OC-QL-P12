from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    """ Contract serializer """
    class Meta:
        model = Contract
        fields = "__all__"
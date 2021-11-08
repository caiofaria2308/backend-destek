from django.db.models import fields
from rest_framework import serializers
from .models import (
    Client,
    Telephone,
    Address,
    Observation,
    Equipment
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields="__all__"


class TelephoneSerializer(serializers.ModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Telephone
        fields = "__all__"


class AddressSerializer(serializers.Serializer):
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"

    
class ObservationSerializer(serializers.Serializer):
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Observation
        fields = "__all__"


class EquipmentSerializer(serializers.Serializer):
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)
    equipment_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Equipment
        fields = "__all__"
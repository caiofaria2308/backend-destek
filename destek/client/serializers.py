from rest_framework import serializers
from .models import (
    Client,
    Telephone,
    Address,
    Observation,
    Equipment
)
from settings.serializers import (
    EquipmentSerializer as SettingEquipmentSerializer
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields="__all__"


class TelephoneSerializer(serializers.ModelSerializer):
    client_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    class Meta:
        model = Telephone
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    client_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"

    
class ObservationSerializer(serializers.ModelSerializer):
    client_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    class Meta:
        model = Observation
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    client_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    equipment_id = serializers.PrimaryKeyRelatedField(read_only=True)
    equipment = SettingEquipmentSerializer(read_only=True)
    class Meta:
        model = Equipment
        fields = "__all__"
from rest_framework import serializers
from .models import (
    Setting as SettingModel,
    Equipment as EquipmentModel,
    EquipmentType as EquipmentTypeModel
)

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingModel
        fields = "__all__"
    

class EquipmentSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = EquipmentModel
        fields = "__all__"


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTypeModel
        fields = "__all__"

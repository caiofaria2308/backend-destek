from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Setting as SettingModel

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingModel
        fields = "__all__"
    
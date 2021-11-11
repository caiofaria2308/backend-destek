from rest_framework import serializers
from .models import Log
from settings.serializers import UserSerializer


class LogSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Log
        fields = "__all__"
from rest_framework import serializers
from .models import (
    Priority,
    Ticket,
    TicketEquipment,
    TicketTracking,
    TicketTrackingFile
)
from client.serializers import (
    ClientSerializer, 
    EquipmentSerializer
)

from settings.serializers import (
    UserSerializer
)


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    priority_id = serializers.UUIDField()
    client_id = serializers.UUIDField()
    user_id = serializers.IntegerField()
    priority = PrioritySerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketEquipmentSerializer(serializers.ModelSerializer):
    ticket_id = serializers.UUIDField()
    ticket = TicketSerializer(read_only=True)
    equipment_id = serializers.UUIDField()
    equipment = EquipmentSerializer(read_only=True)
    
    
    class Meta:
        model = TicketEquipment
        fields = "__all__"


class TicketTrackingSerializer(serializers.ModelSerializer):
    ticket_id = serializers.UUIDField()
    ticket = TicketSerializer(read_only=True)
    user_id = serializers.IntegerField()
    user = UserSerializer(read_only=True)

    
    class Meta:
        model = TicketTracking
        fields = "__all__"


class TicketTrackingFileSerializer(serializers.ModelSerializer):
    ticket_tracking_id = serializers.UUIDField()
    ticket_tracking = TicketTrackingSerializer(read_only=True)


    class Meta:
        model = TicketTrackingFile
        fields = "__all__"

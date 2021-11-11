from django.db.models import fields
from rest_framework import serializers
from .models import (
    Vacation,
    Type,
    VisitQueue
)

from client.serializers import (
    ClientSerializer
)
from settings.serializers import (
    UserSerializer
)
from iticket.serializers import (
    TicketSerializer
)


class VacationSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Vacation
        fields = "__all__"
        
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        
        
class VisitQueueSerializer(serializers.ModelSerializer):
    type_id = serializers.UUIDField()
    type = TypeSerializer(read_only=True)
    user_id = serializers.IntegerField()
    user = UserSerializer(read_only=True)   
    ticket_id = serializers.UUIDField()
    ticket = TicketSerializer(read_only=True)
    client_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    
    class Meta:
        model = VisitQueue
        fields = "__all__"
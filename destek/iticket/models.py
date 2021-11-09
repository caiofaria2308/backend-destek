from django.db import models

from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import uuid


class Priority(models.Model):
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True
    )
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=True
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=128
    )
    color = models.CharField(
        verbose_name="Color",
        max_length=128
    )


class Ticket(models.Model):
    STATUS = (
        (0, 'ABERTO'),
        (1, 'ATRIBUIDO'),
        (2, 'EM ATENDIMENTO'),
        (3, 'AGUARDANDO INTERNAMENTE'),
        (4, 'AGUARDANDO CLIENTE'),
        (5, 'AGUARDANDO TERCEIROS'),
        (6, 'RESOLVIDO'),
        (7, 'NAO RESOLVIDO'),
    )
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True
    )
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=True
    )
    unique_code = models.CharField(
        verbose_name= "Unique code",
        unique=True,
        max_length=20,
        default=str(
            datetime.datetime.utcnow()
            ).replace('-', '')
            .replace(':', '')
            .replace('.', '')
            .replace(' ', '')
    )
    client = models.ForeignKey(
        "client.Client",
        related_name="+",
        on_delete=CASCADE,
        verbose_name="Client",
        editable=True
    )
    user = models.ForeignKey(
        "settings.User",
        related_name="+",
        on_delete=CASCADE,
        verbose_name="Responsible user",
        editable=True,
        null=True,
        blank=True
    )
    priority = models.ForeignKey(
        "iticket.priority",
        related_name="+",
        on_delete=CASCADE,
        verbose_name="Priority",
        editable=True
    )
    status = models.SmallIntegerField(
        default=0,
        choices=STATUS,
        verbose_name="Status"
    )
    title = models.CharField(
        verbose_name="Title",
        max_length=256
    )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    is_closed = models.BooleanField(
        verbose_name="Is closed",
        default=False
    )


    def __str__(self) -> str:
        return f"{self.unique_code} - {self.title}"


class TicketTracking(models.Model):
    STATUS = (
        (0, 'ABERTO'),
        (1, 'ATRIBUIDO'),
        (2, 'EM ATENDIMENTO'),
        (3, 'AGUARDANDO INTERNAMENTE'),
        (4, 'AGUARDANDO CLIENTE'),
        (5, 'AGUARDANDO TERCEIROS'),
        (6, 'RESOLVIDO'),
        (7, 'NAO RESOLVIDO'),
    )
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True
    )
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=True
    )
    ticket = models.ForeignKey(
        'iticket.Ticket',
        related_name='+',
        on_delete=CASCADE,
        verbose_name="Ticket"
    )
    user = models.ForeignKey(
        'settings.User',
        related_name="+",
        on_delete=CASCADE,
        verbose_name="User"
    )
    status = models.SmallIntegerField(
        default=0,
        choices=STATUS,
        verbose_name="Status"
    )
    tracking = models.TextField(
        verbose_name="Tracking"
    )


class TicketTrackingFile(models.Model):
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True
    )
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=True
    )
    ticket_tracking = models.ForeignKey(
        'iticket.TicketTracking',
        related_name='+',
        on_delete=CASCADE,
        verbose_name="Ticket tracking"
    )
    file = models.FileField(
        verbose_name='File'
    )


class TicketEquipment(models.Model):
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True
    )
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=True
    )
    ticket = models.ForeignKey(
        'iticket.Ticket',
        verbose_name='Ticket',
        related_name='+',
        on_delete=CASCADE
    )
    equipment = models.ForeignKey(
        'client.Equipment',
        verbose_name="Cliente equipmente",
        related_name="+",
        on_delete=CASCADE
    )
    observation = models.TextField(
        verbose_name="Observation",
        null=True,
        blank=True
    )   

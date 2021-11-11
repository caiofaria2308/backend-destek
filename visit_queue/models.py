from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import uuid


class Vacation(models.Model):
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
    user = models.ForeignKey(
        "settings.User",
        on_delete=CASCADE,
        verbose_name="User"
    )
    initial_date = models.DateField(
        verbose_name="Initial data"
    )
    final_date = models.DateField(
        verbose_name="Final data"
    )
    
    
class Type(models.Model):
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
        max_length=128,
        verbose_name="Name",
        unique=True
    )
    
    
class VisitQueue(models.Model):
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
    client = models.ForeignKey(
        "client.Client",
        on_delete=CASCADE,
        verbose_name="Client"
    )
    visit_date = models.DateField(
        verbose_name="Date of visit"
    )
    visit_duration = models.SmallIntegerField(
        verbose_name="Durantion of visit"
    )
    type = models.ForeignKey(
        'visit_queue.Type',
        on_delete=CASCADE,
        verbose_name="Type"
    )
    user = models.ForeignKey(
        'settings.User',
        on_delete=CASCADE,
        verbose_name="User",
        null=True,
        blank=True,
    )
    ticket = models.ForeignKey(
        'iticket.Ticket',
        on_delete=CASCADE,
        verbose_name="Ticket",
        null=True,
        blank=True
    )

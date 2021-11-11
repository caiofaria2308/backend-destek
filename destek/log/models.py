from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import uuid

class Log(models.Model):
    TYPE = (
        (0, 'INSERT'),
        (1, 'UPDATE'),
        (2, 'DELETE')
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
    user = models.ForeignKey(
        "settings.User",
        on_delete=CASCADE,
        verbose_name="User"
    )
    table = models.CharField(
        max_length=256,
        verbose_name="Table name"
    )
    primary_key = models.CharField(
        max_length=256,
        verbose_name="Primary key of object"
    )
    data = models.JSONField(
        verbose_name="Data"
    )
    type = models.SmallIntegerField(
        verbose_name="Type",
        choices=TYPE
    )
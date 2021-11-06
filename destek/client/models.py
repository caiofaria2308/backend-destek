from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
from django.db.models.deletion import CASCADE
import uuid

class Client(models.Model): 
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
    reference_code = models.CharField(
        verbose_name="Reference code",
        unique=True,
        max_length=10,
        null=True
    )
    corporate_name = models.CharField(
        verbose_name="Corporate name",
        max_length=256,
        null=True
    )
    fantasy_name = models.CharField(
        verbose_name="Fantasy name",
        max_length=256
    )
    main_document = models.CharField(
        verbose_name="CNPJ or CPF",
        max_length=20,
        unique=True
    )
    secondary_document = models.CharField(
        verbose_name="IE or RG",
        max_length=20,
        null=True
    )
    is_corporate = models.BooleanField(
        verbose_name="Person or entity",
        default=True
    )
    is_active = models.BooleanField(
        verbose_name="if client is active or not",
        default=True
    )


class Telephone(models.Model):
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
        related_name="+", 
        on_delete=CASCADE,
        verbose_name="Client",

        editable=False
    )
    telephone = models.CharField(
        verbose_name="telephone",
        max_length=15
    )

    is_active = models.BooleanField(
        verbose_name="if client is active or not",
        default=True
    )


    class Meta:
        unique_together = (("client", "telephone"),)


class Address(models.Model):
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
        related_name="+", 
        on_delete=CASCADE,
        editable=False,
        verbose_name="Client"
    )
    zip_code = models.CharField(
        verbose_name="ZIP code of adress",
        max_length=10
    )
    address = models.CharField(
        verbose_name="Address",
        max_length=256
    )
    complement = models.CharField(
        verbose_name="Complement of address",
        max_length=256
    )
    number = models.CharField(
        verbose_name="'Number' of Address",
        max_length=10
    )
    district = models.CharField(
        verbose_name="District of address",
        max_length=256
    )
    city = models.CharField(
        verbose_name="City of address",
        max_length=256
    )
    state = models.CharField(
        verbose_name="State of address",
        max_length=2
    )
    is_main = models.BooleanField(
        verbose_name="Is the main address ? ",
        default=True
    )


class Equipment(models.Model):
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
        related_name="+", 
        on_delete=CASCADE,
        editable=False,
        verbose_name="Client"
    )
    equipment = models.ForeignKey(
        "settings.Equipment",
        related_name="+", 
        on_delete=CASCADE,
        editable=False,
        verbose_name="Equipment"
    )


    class Meta:
        unique_together = (("client", "equipment"),)


class Observation(models.Model):
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
        related_name="+", 
        on_delete=CASCADE,
        editable=False,
        verbose_name="Client"
    )
    title = models.CharField(
        verbose_name="Title of observation",
        max_length=256
    )
    information = models.TextField(
        verbose_name="Information"
    )
    file = models.FileField(
        verbose_name="File of observation",
        null=True,
        blank=True
    )
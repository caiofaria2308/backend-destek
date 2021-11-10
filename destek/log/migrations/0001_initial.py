# Generated by Django 3.2.9 on 2021-11-10 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('table', models.CharField(max_length=256, verbose_name='Table name')),
                ('primary_key', models.CharField(max_length=256, verbose_name='Primary key of object')),
                ('data', models.JSONField(verbose_name='Data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]

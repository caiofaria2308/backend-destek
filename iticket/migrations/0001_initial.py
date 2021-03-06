# Generated by Django 3.2.9 on 2021-11-09 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('color', models.CharField(max_length=128, verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('unique_code', models.CharField(default='20211109135119961985', max_length=20, unique=True, verbose_name='Unique code')),
                ('status', models.SmallIntegerField(choices=[(0, 'ABERTO'), (1, 'ATRIBUIDO'), (2, 'EM ATENDIMENTO'), (3, 'AGUARDANDO INTERNAMENTE'), (4, 'AGUARDANDO CLIENTE'), (5, 'AGUARDANDO TERCEIROS'), (6, 'RESOLVIDO'), (7, 'NAO RESOLVIDO')], default=0, verbose_name='Status')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Is closed')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='client.client', verbose_name='Client')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='iticket.priority', verbose_name='Priority')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Responsible user')),
            ],
        ),
        migrations.CreateModel(
            name='TicketTracking',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('status', models.SmallIntegerField(choices=[(0, 'ABERTO'), (1, 'ATRIBUIDO'), (2, 'EM ATENDIMENTO'), (3, 'AGUARDANDO INTERNAMENTE'), (4, 'AGUARDANDO CLIENTE'), (5, 'AGUARDANDO TERCEIROS'), (6, 'RESOLVIDO'), (7, 'NAO RESOLVIDO')], default=0, verbose_name='Status')),
                ('tracking', models.TextField(verbose_name='Tracking')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='iticket.ticket', verbose_name='Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='TicketTrackingFile',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('ticket_tracking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='iticket.tickettracking', verbose_name='Ticket tracking')),
            ],
        ),
        migrations.CreateModel(
            name='TicketEquipment',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Observation')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='client.equipment', verbose_name='Cliente equipmente')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='iticket.ticket', verbose_name='Ticket')),
            ],
        ),
    ]

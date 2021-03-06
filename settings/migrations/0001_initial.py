# Generated by Django 3.2.9 on 2021-11-06 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50, verbose_name='Full name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('phone', models.CharField(max_length=20, null=True, unique=True, verbose_name='cellphone number')),
                ('support', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255, verbose_name='label of setting')),
                ('value', models.TextField(verbose_name='Value of setting')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

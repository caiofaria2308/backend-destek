# Generated by Django 3.2.9 on 2021-11-06 03:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_setting_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-06 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20211106_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settings.equipmenttype'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-18 00:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0043_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('be46d1ce-669d-4eca-94fd-79a2962473e3')),
        ),
    ]

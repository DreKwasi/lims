# Generated by Django 4.0.6 on 2022-08-28 00:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('675a9d0b-ea77-4892-a0fe-760e01d4fda1')),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-21 16:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0071_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('2f40feb6-64b3-4cb0-8480-41c5ecf60a77')),
        ),
    ]

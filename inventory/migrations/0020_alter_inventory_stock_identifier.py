# Generated by Django 4.0.6 on 2022-08-28 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('422ae46f-77d7-427b-a929-8047d02bafd2')),
        ),
    ]

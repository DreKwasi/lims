# Generated by Django 4.0.6 on 2022-09-19 15:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0061_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('11846ef4-fa53-4b1a-a388-016950527a95')),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-18 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0048_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('80357e09-2320-4d28-8f45-a78f54f4f620')),
        ),
    ]

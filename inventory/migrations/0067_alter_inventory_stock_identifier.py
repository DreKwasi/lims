# Generated by Django 4.0.6 on 2022-09-20 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0066_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('dc6ec436-68ef-48b4-91af-650719973d55')),
        ),
    ]

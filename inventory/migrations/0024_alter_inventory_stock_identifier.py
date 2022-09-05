# Generated by Django 4.0.6 on 2022-09-01 23:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('e35f2554-1cdb-459c-b767-deb728857ed1')),
        ),
    ]

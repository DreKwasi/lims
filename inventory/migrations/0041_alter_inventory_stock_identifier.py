# Generated by Django 4.0.6 on 2022-09-04 20:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0040_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('802a7062-7a08-420c-b4eb-f2bf799519ee')),
        ),
    ]

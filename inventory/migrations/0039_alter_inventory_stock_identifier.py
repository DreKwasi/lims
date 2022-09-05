# Generated by Django 4.0.6 on 2022-09-04 20:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0038_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('e30709d2-ad72-4105-a157-8becfa746b77')),
        ),
    ]

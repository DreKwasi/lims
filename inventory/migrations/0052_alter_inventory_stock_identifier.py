# Generated by Django 4.0.6 on 2022-09-18 11:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0051_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('f5462d6c-0bbf-4c37-bf2f-267b5f420e22')),
        ),
    ]

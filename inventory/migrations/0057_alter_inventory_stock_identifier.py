# Generated by Django 4.0.6 on 2022-09-18 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0056_alter_inventory_stock_identifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('c2fdd857-7606-49a0-bd3e-95b5780654a0')),
        ),
    ]

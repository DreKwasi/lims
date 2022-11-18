# Generated by Django 4.0.6 on 2022-09-18 23:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0057_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('d048e4db-a12a-4fcc-9e25-769687f80c40')),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-03 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0034_alter_inventory_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('88956a76-a9f9-44f6-aff8-989dec8da3bb')),
        ),
    ]

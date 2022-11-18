# Generated by Django 4.0.6 on 2022-09-21 16:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0062_alter_identifiedstock_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('36a354a2-fceb-4086-b1a3-cbd52c60dc24'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-28 01:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0017_rename_put_away_putaway_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('0b5c7322-f902-47d4-a5e2-91afe8a5558c'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

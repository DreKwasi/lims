# Generated by Django 4.0.6 on 2022-09-19 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0055_purchaseorderproduct_planned_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('37276b69-c421-4c25-abc1-9951a16d9599'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='planned_quantity',
            field=models.IntegerField(blank=True),
        ),
    ]

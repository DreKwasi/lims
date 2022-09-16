# Generated by Django 4.0.6 on 2022-09-03 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0032_purchaseorder_purchase_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('8ad7f0c1-14a6-4eba-b05e-893340f0f3d3'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

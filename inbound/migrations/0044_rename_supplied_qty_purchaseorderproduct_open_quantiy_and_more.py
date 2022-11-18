# Generated by Django 4.0.6 on 2022-09-18 02:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0043_rename_cost_price_purchaseorderproduct_unit_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorderproduct',
            old_name='supplied_qty',
            new_name='open_quantiy',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='actual_delivery_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseorderproduct',
            name='delivered_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('d2b38d36-0d96-4959-9385-406e1120fc1a'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

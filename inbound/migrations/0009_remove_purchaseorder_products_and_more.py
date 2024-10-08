# Generated by Django 4.0.6 on 2022-08-27 15:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0010_remove_manufacturer_brand_name_and_more'),
        ('inbound', '0008_remove_purchaseorderproduct_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='products',
        ),
        migrations.AddField(
            model_name='purchaseorderproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulary.product_list'),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('27ca5ff3-4a7b-4725-b86a-4ad900cb008c'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

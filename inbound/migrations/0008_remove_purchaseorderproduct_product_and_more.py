# Generated by Django 4.0.6 on 2022-08-27 15:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0010_remove_manufacturer_brand_name_and_more'),
        ('inbound', '0007_purchaseorderproduct_stock_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorderproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='products',
            field=models.ManyToManyField(to='formulary.product_list'),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('37156a11-61d5-480d-89e1-218cf8b91cca'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

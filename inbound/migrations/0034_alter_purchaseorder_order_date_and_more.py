# Generated by Django 4.0.6 on 2022-09-03 16:50

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0033_alter_purchaseorderproduct_stock_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='expiration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('b91ca667-7108-4688-aec0-b0bd49674c72'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

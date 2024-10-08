# Generated by Django 4.0.6 on 2022-09-04 20:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0034_alter_purchaseorder_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('b5847730-2355-4f53-8a16-e76da4484126'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

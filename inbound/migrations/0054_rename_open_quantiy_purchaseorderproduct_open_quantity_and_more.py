# Generated by Django 4.0.6 on 2022-09-18 23:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0053_rename_created_data_identifiedstock_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorderproduct',
            old_name='open_quantiy',
            new_name='open_quantity',
        ),
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('8cad575e-fb2a-4175-bf33-ec3bca9053a0'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
    ]

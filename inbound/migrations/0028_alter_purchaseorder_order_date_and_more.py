# Generated by Django 4.0.6 on 2022-09-03 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_supplier_supplied_products'),
        ('inbound', '0027_alter_purchaseorderproduct_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.supplier'),
        ),
        migrations.AlterField(
            model_name='purchaseorderproduct',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('afcd0902-7091-4e88-9a93-15c010181eba'), editable=False, null=True, verbose_name='unique_identifier'),
        ),
    ]

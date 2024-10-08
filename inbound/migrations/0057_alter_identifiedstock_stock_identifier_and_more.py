# Generated by Django 4.0.6 on 2022-09-19 15:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0056_alter_identifiedstock_stock_identifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('a83513ec-fc1e-4aa5-962d-5744c3efb1fb'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
        migrations.CreateModel(
            name='PurchaseOrderTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered_quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inbound.purchaseorderproduct')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inbound.purchaseorder')),
            ],
        ),
    ]

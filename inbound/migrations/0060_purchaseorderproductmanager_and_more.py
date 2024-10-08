# Generated by Django 4.0.6 on 2022-09-19 15:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0059_rename_purchaseordertransactions_purchaseordertransaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderProductManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('1d1dbfa6-fd46-412f-aad1-5b76e3c7736f'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
    ]

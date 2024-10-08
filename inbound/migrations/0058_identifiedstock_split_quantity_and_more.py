# Generated by Django 4.0.6 on 2022-09-19 15:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0057_alter_identifiedstock_stock_identifier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifiedstock',
            name='split_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('ab1b0461-7a55-4dec-b1e7-4a20eaa2d797'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
    ]

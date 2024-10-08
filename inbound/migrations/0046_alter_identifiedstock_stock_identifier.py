# Generated by Django 4.0.6 on 2022-09-18 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inbound', '0045_rename_put_site_putaway_site_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiedstock',
            name='stock_identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('9f449bd1-ee39-4bce-ac55-c5a76b5e802d'), editable=False, null=True, verbose_name='Unique Identifier'),
        ),
    ]

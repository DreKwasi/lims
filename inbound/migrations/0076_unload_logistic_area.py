# Generated by Django 4.0.6 on 2022-11-14 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0082_remove_inventory_site'),
        ('inbound', '0075_identifiedstock_unload_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unload',
            name='logistic_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.logisticarea'),
        ),
    ]

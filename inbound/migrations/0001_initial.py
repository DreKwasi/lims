# Generated by Django 4.0.6 on 2022-08-27 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulary', '0010_remove_manufacturer_brand_name_and_more'),
        ('inventory', '0005_rename_date_added_site_created_date'),
        ('accounts', '0004_remove_supplier_supplied_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inbound_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=50, verbose_name='Status')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('inbound_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.site')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplied_qty', models.IntegerField()),
                ('cost_price', models.FloatField()),
                ('batch_nummber', models.CharField(max_length=225)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulary.product_list')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inbound.purchaseorder')),
            ],
        ),
    ]

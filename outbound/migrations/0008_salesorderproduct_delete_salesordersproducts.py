# Generated by Django 4.0.6 on 2022-11-23 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_pricelist_created_date_pricelist_updated_date'),
        ('formulary', '0009_alter_unitofmeasure_pack'),
        ('outbound', '0007_rename_stocktransferproducts_stocktransferproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_level', models.IntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_of_measure', models.CharField(choices=[('Packs', 'Packs'), ('Units', 'Units'), ('Volume in Mls', 'Volume in Mls'), ('Weight in Grams', 'Weight in Grams')], default='pack', max_length=20)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Cancelled', 'Cancelled'), ('Not Released', 'Not Released'), ('Partial', 'Partial'), ('Released', 'Released'), ('Delivered', 'Delivered')], default='Not Started', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.pricelist')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formulary_sales_order', to='formulary.productlist')),
                ('sales_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_order_products', to='outbound.salesorder')),
            ],
        ),
        migrations.DeleteModel(
            name='SalesOrdersProducts',
        ),
    ]

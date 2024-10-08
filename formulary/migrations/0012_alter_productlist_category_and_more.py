# Generated by Django 4.0.6 on 2022-09-18 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulary', '0011_rename_product_list_productlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_prooducts', to='formulary.category'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer_products', to='formulary.manufacturer'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='product_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='form_product', to='formulary.form'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='unit_of_measure',
            field=models.IntegerField(verbose_name='Pack Size'),
        ),
    ]

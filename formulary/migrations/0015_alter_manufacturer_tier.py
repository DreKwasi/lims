# Generated by Django 4.0.6 on 2022-09-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0014_productlist_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='tier',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

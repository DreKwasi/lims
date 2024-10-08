# Generated by Django 4.0.6 on 2022-09-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_supplier_supplied_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_location',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='email_address',
            new_name='email',
        ),
        migrations.AddField(
            model_name='supplier',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

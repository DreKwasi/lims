# Generated by Django 4.0.6 on 2022-08-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

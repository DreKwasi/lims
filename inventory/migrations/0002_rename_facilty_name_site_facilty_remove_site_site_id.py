# Generated by Django 4.0.6 on 2022-08-24 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='facilty_name',
            new_name='facilty',
        ),
        migrations.RemoveField(
            model_name='site',
            name='site_id',
        ),
    ]

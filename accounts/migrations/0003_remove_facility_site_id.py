# Generated by Django 4.0.6 on 2022-08-24 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='site_id',
        ),
    ]

# Generated by Django 4.0.6 on 2022-11-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0006_alter_unitofmeasure_gram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitofmeasure',
            name='unit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit'),
        ),
    ]

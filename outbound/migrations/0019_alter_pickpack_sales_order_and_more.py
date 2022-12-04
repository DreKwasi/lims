# Generated by Django 4.0.6 on 2022-12-04 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outbound', '0018_remove_pickpack_user_pickpack_user_ordered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickpack',
            name='sales_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_order_picks', to='outbound.stocktransfer'),
        ),
        migrations.AlterField(
            model_name='pickpack',
            name='user_processed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_processed_pickpack', to=settings.AUTH_USER_MODEL),
        ),
    ]

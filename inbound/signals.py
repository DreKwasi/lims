from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from .queryset import post_update
from .models import *


def create_putaway(sender, instance, created, **kwargs):
    if created:
        if instance.status == "Finished":
            status = "Not Started"
            put_site = instance.site_id
            put_area = instance.unload_area
            final_unload = instance
            Put_Away.objects.create(
                status=status,
                put_site=put_site,
                put_area=put_area,
                final_unload=final_unload,
            )
            print("PutAway Created !!")
    if not created:
        if instance.status == "Finished":
            status = "Not Started"
            put_site = instance.site_id
            put_area = instance.unload_area
            final_unload = instance
            Put_Away.objects.get_or_create(
                status=status,
                put_site=put_site,
                put_area=put_area,
                final_unload=final_unload,
            )
            print("PutAway Updated/Created !!")


post_save.connect(create_putaway, Unload)
post_update.connect(create_putaway, Unload)

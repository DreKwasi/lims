from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from .queryset import post_update
from .models import *


def create_putaway(sender, instance, created, **kwargs):
    if created:
        if instance.status == "Finished":
            status = "Not Started"
            put_site = instance.site_id
            final_unload = instance
            PutAway.objects.create(
                status=status,
                put_site=put_site,
                final_unload=final_unload,
            )
            print("PutAway Created !!")
    if not created:
        if instance.status == "Finished":
            status = "Not Started"
            put_site = instance.site_id
            final_unload = instance
            PutAway.objects.get_or_create(
                status=status,
                put_site=put_site,
                final_unload=final_unload,
            )
            print("PutAway Updated/Created !!")


post_save.connect(create_putaway, Unload)
post_update.connect(create_putaway, Unload)

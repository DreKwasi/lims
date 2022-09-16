from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from inbound.models import PutAway

from .models import *
from .models import Inventory


def create_inventory(sender, instance, created, **kwargs):
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
        created (_type_): _description_
    """
    if created:
        if instance.status == "Finished":
            putaways = instance.putaway_products.all()
            for putaway in putaways:
                product = putaway.product
                batch = putaway.batch
                expiration_date = putaway.expiration_date
                pack_quantity = putaway.unload_qty
                logistic_area = putaway.put_area
                stock_identifier = putaway.stock_id
                Inventory.objects.create(
                    product=product,
                    batch=batch,
                    pack_quantity=pack_quantity,
                    logistic_area=logistic_area,
                    stock_type="Warehouse",
                    expiration_date=expiration_date,
                    stock_identifier=stock_identifier,
                )
                print("Inventory Created !!")

    if not created:
        if instance.status == "Finished":
            putaways = instance.putaway_products.all()
            for putaway in putaways:
                product = putaway.product
                batch = putaway.batch
                expiration_date = putaway.expiration_date
                pack_quantity = putaway.unload_qty
                logistic_area = putaway.put_area
                stock_identifier = putaway.stock_id
                Inventory.objects.create(
                    product=product,
                    batch=batch,
                    pack_quantity=pack_quantity,
                    logistic_area=logistic_area,
                    stock_type="Warehouse",
                    expiration_date=expiration_date,
                    stock_identifier=stock_identifier,
                )
                print("Inventory Created !!")


post_save.connect(create_inventory, PutAway)

from django.db.models.signals import post_save

from .models import Inventory
from inbound.models import Unload
import random


def check_area(product, site_id):
    areas = site_id.areas.all()
    stock = Inventory.objects.filter(product=product)
    filtered = [x for x in stock if x.site_id == site_id]
    if filtered:
        return filtered[0].logistic_area
    else:
        return random.choice(areas)


def create_inventory(sender, instance, created, **kwargs):

    if not created:
        if instance.status == "In Process":

            for product in instance.unload_products.all():
                objs = []
                for stk in product.identified_stock.all():
                    stock_identifier = stk.stock_identifier
                    pack_quantity = stk.split_quantity
                    batch = stk.batch_number
                    expiration_date = stk.expiration_date

                    objs.append(
                        Inventory(
                            product=product.product,
                            batch=batch,
                            pack_quantity=pack_quantity,
                            logistic_area=check_area(
                                product.product, instance.site_id
                            )
                            if stk.target_logistic_area == None
                            else stk.target_logistic_area,
                            stock_type="Warehouse",
                            expiration_date=expiration_date,
                            stock_identifier=stock_identifier,
                        )
                    )

                Inventory.objects.bulk_create(objs)
            print("Inventory Created !!")


post_save.connect(create_inventory, Unload)

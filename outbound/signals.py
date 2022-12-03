from collections import defaultdict

from django.db.models.signals import post_save

from inventory.models import Inventory

from .models import (
    Delivery,
    DeliveryProduct,
    PickPack,
    PickPackProduct,
    StockTransfer,
    StockTransferProduct,
)


def inventory_locator(requested_qty, inventory_qs):

    item_dict = defaultdict(list)
    remainder_qty = requested_qty

    for item in inventory_qs:
        item_dict["batch_number"].append(item.batch_number)
        item_dict["expiration_date"].append(item.expiration_date)
        item_dict["stock_identifier"].append(item.stock_identifier)
        item_dict["logistic_area"].append(item.logistic_area)

        if remainder_qty > item.pack_quantity:
            remainder_qty -= item.pack_quantity
            item_dict["pack_quantity"].append(item.pack_quantity)
        elif remainder_qty <= item.pack_quantity:
            item_dict["pack_quantity"].append(remainder_qty)
            break

    return item_dict


def create_pick_pack(sender, instance, created, **kwargs):
    print("called")
    if instance.status == "Partial":
        if [x.inventory_level for x in instance.stock_transfer_products.all()]:
            pick_pack = PickPack(
                ship_to_location=instance.ship_to_location,
                ship_from_location=instance.ship_from_location,
                order_priority=instance.order_priority,
            )
            prev_pick_packs = PickPack.objects.filter(
                stock_transfer_order=instance,
            )
            pp_product_objs = []
            for st_product in instance.stock_transfer_products.all():
                if st_product.inventory_level:
                    prev_qty = 0
                    if prev_pick_packs:
                        for prev_pick_pack in prev_pick_packs:
                            try:
                                pp_product = (
                                    prev_pick_pack.pickpack_products.get(
                                        product=st_product
                                    )
                                )
                                prev_qty += pp_product.quantity
                            except Exception as e:
                                print(e)
                                continue

                    requested_qty = st_product.quantity - prev_qty
                    inventory_qs = Inventory.objects.filter(
                        product=st_product
                    ).order_by("expiration_date")

                    inv_dict = inventory_locator(requested_qty, inventory_qs)
                    for index, batch in enumerate(inv_dict["batch_number"]):
                        pp_product = PickPackProduct(
                            pickpack=pick_pack,
                            product=st_product,
                            batch_number=batch,
                            quantity=inv_dict["pack_quantity"][index],
                            logistic_area=inv_dict["logistic_area"][index],
                            expiration_date=inv_dict["expiration_date"][index],
                            stock_identifier=inv_dict["stock_identifier"][
                                index
                            ],
                            unit_of_measure=st_product.unit_of_measure,
                        )

                        pp_product_objs.append(pp_product)

            if pp_product_objs:
                PickPack.objects.create(pick_pack)
                PickPackProduct.objects.bulk_create(pp_product_objs)


post_save.connect(create_pick_pack, StockTransfer)

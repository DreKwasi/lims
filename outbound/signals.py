import itertools
from collections import defaultdict

from django.db.models.signals import post_save
from django.db.models.query import Q

from inventory.models import Inventory, Site

from .models import (
    Delivery,
    DeliveryProduct,
    PickPack,
    PickPackProduct,
    StockTransfer,
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
            item.update(stock_type="Pre-Delivered")

        elif remainder_qty < item.pack_quantity:
            diff = item.pack_quantity - remainder_qty
            item_dict["pack_quantity"].append(remainder_qty)
            item.pack_quantity = diff
            item.save()

            item.pk, item.pack_quantity, item.stock_type = (
                None,
                remainder_qty,
                "Pre-Delivered",
            )
            item.save()
            break

        elif remainder_qty == item.pack_quantity:
            item_dict["pack_quantity"].append(remainder_qty)
            item.update(stock_type="Pre-Delivered")
            break

    return item_dict


def create_pick_pack(sender, instance, created, **kwargs):
    if instance.status in ["Partial", "Finished"]:
        if any(
            x.inventory_level for x in instance.stock_transfer_products.all()
        ):
            pick_pack = PickPack(
                stock_transfer_order=instance,
                ship_to_location=instance.ship_to_location,
                ship_from_location=instance.ship_from_location,
                order_priority=instance.order_priority,
                user_ordered=instance.user,
            )
            prev_picks = instance.stock_transfer_picks.filter(
                ~Q(status="Cancelled")
            )
            prev_picks_products = list(
                itertools.chain.from_iterable(
                    [x.pickpack_products.all() for x in prev_picks]
                )
            )

            pp_product_objs = []
            st_products = instance.stock_transfer_products.filter(
                Q(status__in=["Not Started", "Not Released", "Partial"])
            )
            for st_product in st_products:
                prev_qty = sum(
                    [
                        x.quantity
                        for x in prev_picks_products
                        if x.product == st_product.product
                    ]
                )

                requested_qty = st_product.quantity - prev_qty

                if requested_qty > 0 and st_product.inventory_level > 0:

                    ship_from = Site.objects.get(
                        facility=instance.ship_from_location
                    )

                    inventory_qs = Inventory.objects.filter(
                        product=st_product.product,
                        stock_type="Warehouse",
                        site=ship_from,
                    ).order_by("expiration_date")

                    inv_dict = inventory_locator(requested_qty, inventory_qs)

                    pp_product_objs = [
                        PickPackProduct(
                            pickpack=pick_pack,
                            product=st_product.product,
                            batch_number=batch,
                            quantity=inv_dict["pack_quantity"][index],
                            logistic_area=inv_dict["logistic_area"][index],
                            expiration_date=inv_dict["expiration_date"][index],
                            stock_identifier=inv_dict["stock_identifier"][
                                index
                            ],
                            unit_of_measure=st_product.unit_of_measure,
                        )
                        for index, batch in enumerate(inv_dict["batch_number"])
                    ]
                    st_product.update(
                        status="Released"
                        if sum(inv_dict["pack_quantity"]) == requested_qty
                        else "Partial"
                    )
            if pp_product_objs:
                pick_pack.save()
                PickPackProduct.objects.bulk_create(pp_product_objs)


post_save.connect(create_pick_pack, StockTransfer)


# def cancel_pick_product(product):
#     product.status = "Cancelled"
#     product.save()


# # def restart_st_product(product):
# #     product.status = "Not Started"
# #     product.save()


# # def cancel_pick_pack(sender, instance, created, **kwargs):
# #     if instance.status == "Cancelled":
# #         pick_products = instance.pick_products.all().values_list("product", flat=True)
# #         stock_transfer = instance.stock_transfer_order
# #         stock_transfer.stock_transfer_products.filter(product__in=pick_products & Q(status="Released") | Q(status="Partial")).update(status="Not ")
# #         map(
# #             cancel_pick_pack,
# #             instance.pick_products.filter(~Q(status="Cancelled")),
# #         )


# # post_save.connect(cancel_pick_pack, PickPack)


def create_delivery_note(sender, instance, created, **kwargs):
    pass


post_save.connect(create_delivery_note, PickPack)

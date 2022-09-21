import random

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from inventory.models import Inventory

from .models import *


def check_area(product):
    stock = Inventory.objects.filter(product=product)
    if stock:
        return stock[0].logistic_area
    else:
        return random.choice(LogisticArea.objects.all())


def update_open_quantity(sender, instance, **kwargs):
    if instance.id:
        instance.open_quantity = (
            instance.planned_quantity - instance.delivered_quantity
        )

    else:
        instance.planned_quantity = instance.open_quantity
        if instance.delivered_quantity != 0:
            instance.open_quantity = (
                instance.planned_quantity - instance.delivered_quantity
            )


def create_unload(sender, instance, created, **kwargs):
    if instance.order_status == "Pending":
        purchase_order = instance
        status = "Not Started"
        site_id = instance.site_id
        target_area = instance.site_id.areas.get(area_name="REC_BAY")
        Unload.objects.create(
            status=status,
            site_id=site_id,
            target_logistic_area=target_area,
            purchase_order=purchase_order,
        )


def create_unload_product(sender, instance, created, **kwargs):
    print(instance.purchase_order.order_status)
    if instance.purchase_order.order_status == "Pending":
        PurchaseOrderTransaction.objects.create(
            product=instance,
            purchase_order=instance.purchase_order,
            delivered_quantity=instance.delivered_quantity,
        )
        transactions = PurchaseOrderTransaction.objects.filter(
            product=instance, purchase_order=instance.purchase_order
        ).order_by("-id")

        try:
            open_quantity = (
                transactions[0].delivered_quantity
                - transactions[1].delivered_quantity
            )
        except Exception:
            open_quantity = transactions[0].delivered_quantity

        unload = instance.purchase_order.unload_set.all().last()
        UnloadProduct.objects.create(
            unload=unload,
            purchase_product=instance,
            open_quantity=open_quantity,
        )


def create_putaway(sender, instance, created, **kwargs):

    if not created:
        if instance.status == "Finished":
            status = "Not Started"
            site_id = instance.site_id
            final_unload = instance
            source_area = instance.target_logistic_area

            putaway = PutAway.objects.create(
                status=status,
                site_id=site_id,
                final_unload=final_unload,
                source_logistic_area=source_area,
            )

            for product in instance.unload_products.all():
                objs = []
                for stk in product.identified_stock.all():
                    stock_identifier = stk.stock_identifier
                    open_quantity = stk.split_quantity
                    batch = stk.batch_number
                    expiration_date = stk.expiration_date

                    objs.append(
                        PutAwayProduct(
                            putaway=putaway,
                            unload_product=product,
                            target_logistic_area=check_area(
                                product.purchase_product.product
                            ),
                            open_quantity=open_quantity,
                            batch=batch,
                            expiration_date=expiration_date,
                            stock_identifier=stock_identifier,
                        )
                    )

                PutAwayProduct.objects.bulk_create(objs)
            print("PutAway Created !!")


pre_save.connect(update_open_quantity, PurchaseOrderProduct)
post_save.connect(create_putaway, Unload)
post_save.connect(create_unload, PurchaseOrder)
post_save.connect(create_unload_product, PurchaseOrderProduct)

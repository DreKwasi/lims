from django.db.models.signals import post_save

from .models import *


def create_unload(sender, instance, created, **kwargs):
    print("called")
    if instance.order_status == "Pending":
        purchase_order = instance
        status = "Not Started"
        site_id = instance.facility.site
        areas = instance.facility.site.areas.all()
        target_area = areas.filter(area_name__icontains="REC_BAY")[0]
        unload = Unload.objects.create(
            status=status,
            site_id=site_id,
            logistic_area=target_area,
            purchase_order=purchase_order,
        )

        objs = map(
            lambda product: PurchaseOrderTransaction(
                product=product,
                purchase_order=instance,
                delivered_quantity=product.delivered_quantity,
            ),
            instance.po_products.all(),
        )
        PurchaseOrderTransaction.objects.bulk_create(list(objs))

        objs = []
        for product in instance.po_products.all():
            transactions = PurchaseOrderTransaction.objects.filter(
                product=product,
                purchase_order=instance,
            ).order_by("-id")

            try:
                open_quantity = (
                    transactions[0].delivered_quantity
                    - transactions[1].delivered_quantity
                )
            except Exception:
                open_quantity = transactions[0].delivered_quantity

            unload_product = UnloadProduct(
                unload=unload,
                product=product.product,
                open_quantity=open_quantity,
                planned_quantity=open_quantity,
                unit_of_measure=product.unit_of_measure,
            )
            objs.append(unload_product)

        UnloadProduct.objects.bulk_create(objs)


post_save.connect(create_unload, PurchaseOrder)

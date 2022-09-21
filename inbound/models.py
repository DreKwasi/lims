import uuid
from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _
from inventory.models import LogisticArea

from .model_managers import (
    PurchaseOrderManager,
    PurchaseOrderProductManager,
    PutAwayManager,
    UnloadManager,
)


class PurchaseOrder(models.Model):
    inbound_status_choices = (
        ("Ordered", "Ordered"),
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )
    payment_terms_choices = (
        ("90 days due net", "90 days due net"),
        ("60 days due net", "60 days due net"),
        ("30 days due net", "60 days due net"),
        ("15 days due net", "15 days due net"),
        ("Pay In Advance", "Pay In Advance"),
        ("Cash On Delivery", "Cash On Delivery"),
        ("Cash In Advance", "Cash In Advance"),
    )

    purchase_order_id = models.CharField(max_length=200, null=True, blank=True)
    supplier = models.ForeignKey(
        "accounts.supplier", on_delete=models.CASCADE, null=True, blank=True
    )
    order_status = models.CharField(
        max_length=50,
        choices=inbound_status_choices,
        verbose_name=_("Order Status"),
        default="Ordered",
    )
    facility = models.ForeignKey(
        "accounts.facility", on_delete=models.SET_NULL, null=True
    )
    site_id = models.ForeignKey(
        "inventory.site", on_delete=models.SET_NULL, null=True
    )
    reference_id = models.CharField(max_length=100, blank=True, null=True)

    products = models.ManyToManyField(
        "formulary.productlist",
        through="PurchaseOrderProduct",
        related_name="purchaseorders",
    )
    order_date = models.DateField(default=date.today)
    payment_terms = models.CharField(
        max_length=100, choices=payment_terms_choices, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    actual_delivery_date = models.DateTimeField(null=True)
    updated_date = models.DateField(auto_now=True)

    objects = PurchaseOrderManager()

    def __str__(self):
        return f"PO-{self.pk}"

    @property
    def total_value(self):
        all_product_objs = self.purchaseorderproduct_set.all()
        product_values = [
            x.cost_price * x.supplied_qty for x in all_product_objs
        ]
        return sum(product_values)


class PurchaseOrderProduct(models.Model):
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        null=True,
        related_name="po_products",
    )
    product = models.ForeignKey(
        "formulary.productlist", on_delete=models.CASCADE, null=True
    )
    open_quantity = models.IntegerField()
    delivered_quantity = models.IntegerField(default=0)
    planned_quantity = models.IntegerField(blank=True)
    unit_price = models.FloatField()
    discount = models.FloatField(max_length=5, null=True, default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = PurchaseOrderProductManager()

    @property
    def product_name(self):
        return self.product.product_name

    def __str__(self):
        return self.product_name


class PurchaseOrderTransaction(models.Model):
    product = models.ForeignKey(PurchaseOrderProduct, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    delivered_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.purchase_order.__str__()


class Unload(models.Model):
    status_choices = (
        ("Not Started", "Not Started"),
        ("In Process", "In Process"),
        ("Finished", "Finished"),
    )

    site_id = models.ForeignKey(
        "inventory.site", on_delete=models.SET_NULL, null=True
    )
    target_logistic_area = models.ForeignKey(
        LogisticArea,
        null=True,
        on_delete=models.SET_NULL,
    )
    status = models.CharField(
        choices=status_choices, max_length=15, default="Not Started"
    )
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE, null=True
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UnloadManager()

    @property
    def unload_id(self):
        return f"UNLOAD-{self.pk}"

    def __str__(self):
        return self.unload_id


class UnloadProduct(models.Model):
    unload = models.ForeignKey(
        Unload, on_delete=models.CASCADE, related_name="unload_products"
    )
    purchase_product = models.ForeignKey(
        PurchaseOrderProduct,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    open_quantity = models.IntegerField(default=0)
    actual_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.purchase_product.product_name

    @property
    def product_name(self):
        return self.purchase_product.product_name

    @property
    def product(self):
        return self.purchase_product.product


class IdentifiedStock(models.Model):
    batch_number = models.CharField(max_length=225, null=True, blank=True)
    expiration_date = models.DateField()
    stock_identifier = models.UUIDField(
        verbose_name=_("Unique Identifier"),
        default=uuid.uuid4(),
        editable=False,
        null=True,
        blank=True,
    )
    unload = models.ForeignKey(
        UnloadProduct,
        on_delete=models.SET_NULL,
        null=True,
        related_name="identified_stock",
    )
    split_quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.batch_number


class PutAway(models.Model):
    status_choices = (
        ("Not Started", "Not Started"),
        ("In Process", "In Process"),
        ("Finished", "Finished"),
    )

    site_id = models.ForeignKey(
        "inventory.site", null=True, on_delete=models.SET_NULL
    )
    final_unload = models.ForeignKey(
        Unload, on_delete=models.CASCADE, null=True
    )
    source_logistic_area = models.ForeignKey(
        "inventory.logisticarea", null=True, on_delete=models.SET_NULL
    )
    status = models.CharField(
        choices=status_choices,
        max_length=15,
        null=True,
        blank=True,
        default="Not Started",
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = PutAwayManager()

    @property
    def put_away_id(self):
        return f"PUT-{self.pk}"

    def __str__(self) -> str:
        return self.put_away_id


class PutAwayProduct(models.Model):
    putaway = models.ForeignKey(
        PutAway, on_delete=models.CASCADE, related_name="putaway_products"
    )
    unload_product = models.ForeignKey(
        UnloadProduct,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    target_logistic_area = models.ForeignKey(
        LogisticArea, null=True, on_delete=models.SET_NULL
    )
    open_quantity = models.IntegerField()
    actual_quantity = models.IntegerField(default=0)
    batch = models.CharField(max_length=50, null=True, blank=True)
    expiration_date = models.DateField()
    stock_identifier = models.UUIDField()

    def __str__(self):
        return self.unload_product.product_name

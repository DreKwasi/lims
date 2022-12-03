import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.models import Inventory

from .model_managers import (
    DeliveryManager,
    PickPackManager,
    StockTransferManager,
)

# Create your models here.


class StockTransfer(models.Model):
    order_priority_choices = (("Normal", "Normal"), ("Urgent", "Urgent"))
    status_choices = (
        ("Cancelled", "Cancelled"),
        ("Partial", "Partial"),
        ("Finished", "Finished"),
        ("Delivered", "Delivered"),
        ("Not Started", "Not Started"),
    )
    ship_to_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_transfers",
        on_delete=models.SET_NULL,
        null=True,
    )
    ship_from_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_receipts",
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.CharField(
        max_length=20, choices=status_choices, default="Not Started"
    )
    order_priority = models.CharField(
        choices=order_priority_choices, default="Normal", max_length=10
    )
    user = models.ForeignKey(
        "accounts.account",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_transfers",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = StockTransferManager()

    def __str__(self):
        return f"ST-{self.id}"


class StockTransferProduct(models.Model):
    uom_choices = (
        ("Packs", "Packs"),
        ("Units", "Units"),
        ("Volume in Mls", "Volume in Mls"),
        ("Weight in Grams", "Weight in Grams"),
    )
    status_choices = (
        ("Not Started", "Not Started"),
        ("Cancelled", "Cancelled"),
        ("Not Released", "Not Released"),
        ("Partial", "Partial"),
        ("Released", "Released"),
        ("Delivered", "Delivered"),
    )
    stock_transfer_order = models.ForeignKey(
        StockTransfer,
        related_name="stock_transfer_products",
        on_delete=models.CASCADE,
        null=True,
    )
    product = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="formulary_stock_transfer",
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_of_measure = models.CharField(
        max_length=20, choices=uom_choices, default="Packs"
    )
    status = models.CharField(
        max_length=20, default="Not Started", choices=status_choices
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def inventory_level(self):
        batch_qtys = Inventory.objects.filter(
            product=self.product
        ).values_list("pack_quantity", flat=True)
        return sum(batch_qtys)


class PickPack(models.Model):
    order_priority_choices = (("Normal", "Normal"), ("Urgent", "Urgent"))
    status_choices = (
        ("Cancelled", "Cancelled"),
        ("Finished", "Finished"),
        ("Not Started", "Not Started"),
    )
    stock_transfer_order = models.ForeignKey(
        StockTransfer,
        related_name="stock_transfer_picks",
        on_delete=models.CASCADE,
        null=True,
    )
    sales_order = models.ForeignKey(
        StockTransfer,
        related_name="sales_order_picks",
        on_delete=models.CASCADE,
        null=True,
    )
    ship_to_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_packs",
        on_delete=models.SET_NULL,
        null=True,
    )
    ship_from_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_picks",
        on_delete=models.SET_NULL,
        null=True,
    )

    status = models.CharField(
        max_length=20, choices=status_choices, default="Not Started"
    )
    order_priority = models.CharField(
        choices=order_priority_choices, default="Normal", max_length=10
    )
    user = models.ForeignKey(
        "accounts.account",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_pickpack",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = PickPackManager()

    def __str__(self):
        return f"PP-{self.id}"


class PickPackProduct(models.Model):
    uom_choices = (
        ("Packs", "Packs"),
        ("Units", "Units"),
        ("Volume in Mls", "Volume in Mls"),
        ("Weight in Grams", "Weight in Grams"),
    )
    pickpack = models.ForeignKey(
        PickPack,
        related_name="pickpack_products",
        on_delete=models.CASCADE,
        null=True,
    )
    product = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="formulary_pickpack",
    )
    quantity = models.PositiveIntegerField(default=1)
    logistic_area = models.ForeignKey(
        "inventory.logisticarea", on_delete=models.SET_NULL, null=True
    )
    batch_number = models.CharField(max_length=225, null=True, blank=True)
    expiration_date = models.DateField()
    stock_identifier = models.UUIDField(
        verbose_name=_("Unique Identifier"),
        editable=False,
        null=True,
        blank=True,
        unique=True,
    )
    unit_of_measure = models.CharField(
        max_length=20, choices=uom_choices, default="Packs"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Delivery(models.Model):
    order_priority_choices = (("Normal", "Normal"), ("Urgent", "Urgent"))
    status_choices = (
        ("Cancelled", "Cancelled"),
        ("Finished", "Finished"),
        ("Not Started", "Not Started"),
    )
    ship_to_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_ship_to",
        on_delete=models.SET_NULL,
        null=True,
    )
    ship_from_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_ship_from",
        on_delete=models.SET_NULL,
        null=True,
    )

    status = models.CharField(
        max_length=20, choices=status_choices, default="Not Started"
    )
    order_priority = models.CharField(
        choices=order_priority_choices, default="Normal", max_length=10
    )
    user = models.ForeignKey(
        "accounts.account",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_delivery",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = DeliveryManager()

    def __str__(self):
        return f"DEL-{self.id}"

    class Meta:
        verbose_name_plural = _("Deliveries")


class DeliveryProduct(models.Model):
    uom_choices = (
        ("Packs", "Packs"),
        ("Units", "Units"),
        ("Volume in Mls", "Volume in Mls"),
        ("Weight in Grams", "Weight in Grams"),
    )
    delivery = models.ForeignKey(
        Delivery,
        related_name="delivery_products",
        on_delete=models.CASCADE,
        null=True,
    )
    product = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="formulary_delivery",
    )
    quantity = models.PositiveIntegerField(default=1)
    logistic_area = models.ForeignKey(
        "inventory.logisticarea", on_delete=models.SET_NULL, null=True
    )
    batch_number = models.CharField(max_length=225, null=True, blank=True)
    expiration_date = models.DateField()
    stock_identifier = models.UUIDField(
        verbose_name=_("Unique Identifier"),
        editable=False,
        null=True,
        blank=True,
        unique=True,
    )
    unit_of_measure = models.CharField(
        max_length=20, choices=uom_choices, default="Packs"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class SalesOrder(models.Model):
    order_priority_choices = (("Normal", "Normal"), ("Urgent", "Urgent"))
    status_choices = (
        ("Not Started", "Not Started"),
        ("Cancelled", "Cancelled"),
        ("Partial", "Partial"),
        ("Finished", "Finished"),
        ("Delivered", "Delivered"),
    )
    account = models.ForeignKey(
        "accounts.facility",
        related_name="account_sales_orders",
        on_delete=models.SET_NULL,
        null=True,
    )
    user = models.ForeignKey(
        "accounts.account",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_sales",
    )
    order_priority = models.CharField(
        choices=order_priority_choices, default="Normal", max_length=20
    )
    status = models.CharField(
        choices=status_choices, default="Not Started", max_length=20
    )
    external_reference = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SO-{self.id}"


class SalesOrderProduct(models.Model):
    uom_choices = (
        ("Packs", "Packs"),
        ("Units", "Units"),
        ("Volume in Mls", "Volume in Mls"),
        ("Weight in Grams", "Weight in Grams"),
    )
    status_choices = (
        ("Not Started", "Not Started"),
        ("Cancelled", "Cancelled"),
        ("Not Released", "Not Released"),
        ("Partial", "Partial"),
        ("Released", "Released"),
        ("Delivered", "Delivered"),
    )
    sales_order = models.ForeignKey(
        SalesOrder,
        related_name="sales_order_products",
        on_delete=models.CASCADE,
        null=True,
    )
    product = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="formulary_sales_order",
    )
    price = models.ForeignKey(
        "billing.pricelist", on_delete=models.SET_NULL, null=True
    )
    inventory_level = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    ship_from_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_sales_transfers",
        on_delete=models.SET_NULL,
        null=True,
    )
    unit_of_measure = models.CharField(
        max_length=20, choices=uom_choices, default="pack"
    )
    status = models.CharField(
        max_length=20, choices=status_choices, default="Not Started"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

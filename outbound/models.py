from django.db import models

# Create your models here.


class StockTransfer(models.Model):
    order_priority_choices = (("Normal", "Normal"), ("Urgent", "Urgent"))
    status_choices = (
        ("Cancelled", "Cancelled"),
        ("Partial", "Partial"),
        ("Finished", "Finished"),
        ("Delivered", "Delivered"),
    )
    ship_to_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_sent_transfers",
        on_delete=models.SET_NULL,
        null=True,
    )
    ship_from_location = models.ForeignKey(
        "accounts.facility",
        related_name="facility_receive_transfers",
        on_delete=models.SET_NULL,
        null=True,
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

    def __str__(self):
        return f"ST-{self.id}"


class StockTransferProducts(models.Model):
    uom_choices = (
        ("pack", "pack(s)"),
        ("batch", "batch"),
        ("volume", "volume"),
        ("weight", "weight"),
        ("unit", "unit"),
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
    products = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="formulary_stock_transfer",
    )
    inventory_level = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    unit_of_measure = models.CharField(max_length=20, choices=uom_choices)
    status = models.CharField(
        max_length=20, default="Not Started", choices=status_choices
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
    order_priority = models.CharField(
        choices=order_priority_choices, default="Normal", max_length=20
    )
    status = models.CharField(
        choices=status_choices, default="Not Started", max_length=20
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class SalesOrdersProducts(models.Model):
    uom_choices = (
        ("pack", "pack"),
        ("batch", "batch"),
        ("volume", "volume"),
        ("kg", "kg"),
        ("unit", "unit"),
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
        related_name="sales_order_products",
        on_delete=models.CASCADE,
        null=True,
    )
    products = models.ForeignKey(
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
    unit_of_measure = models.CharField(
        max_length=20, choices=uom_choices, default="pack"
    )
    status = models.CharField(
        max_length=20, choices=status_choices, default="Not Started"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

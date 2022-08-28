import uuid

from django.db import models

from .model_managers import PutAwayManager, UnloadManager


class PurchaseOrder(models.Model):
    inbound_status_choices = (
        ("Ordered", "Ordered"),
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )

    supplier = models.ForeignKey("accounts.supplier", on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=50,
        choices=inbound_status_choices,
        verbose_name="Status",
        default="Ordered",
    )
    facility = models.ForeignKey(
        "accounts.facility", on_delete=models.SET_NULL, null=True
    )
    products = models.ManyToManyField(
        "formulary.productlist",
        through="PurchaseOrderProduct",
        related_name="purchaseorders",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    @property
    def reference_id(self):
        return f"PO-{self.pk}"

    def __str__(self):
        return self.reference_id


class PurchaseOrderProduct(models.Model):
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE, null=True
    )
    product = models.ForeignKey(
        "formulary.productlist", on_delete=models.CASCADE, null=True
    )
    supplied_qty = models.IntegerField()
    cost_price = models.FloatField()
    batch_number = models.CharField(max_length=225)
    expiration_date = models.DateTimeField()
    stock_identifier = models.UUIDField(
        verbose_name="unique_identifier",
        default=uuid.uuid4(),
        editable=False,
        null=True,
        blank=True,
    )
    discount = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def product_name(self):
        return self.product.product_name

    def __str__(self):
        return self.product_name


class Unload(models.Model):
    status_choices = (
        ("Not Started", "Not Started"),
        ("In Process", "In Process"),
        ("Finished", "Finished"),
    )

    site_id = models.ForeignKey(
        "inventory.site", on_delete=models.SET_NULL, null=True
    )
    unload_area = models.ForeignKey(
        "inventory.logisticarea",
        default="REC_BAY",
        on_delete=models.SET_DEFAULT,
    )
    status = models.CharField(
        choices=status_choices, max_length=15, default="Not Started"
    )
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)

    objects = UnloadManager()

    @property
    def unload_id(self):
        return f"UNLOAD-{self.pk}"

    def __str__(self):
        return self.unload_id


class UnloadProduct(models.Model):
    unload = models.ForeignKey(
        Unload, on_delete=models.CASCADE, related_name="products"
    )
    purchase_product = models.ForeignKey(
        PurchaseOrderProduct,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unload_qty = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def product_name(self):
        return self.purchase_product.product_name

    def __str__(self):
        return self.purchase_product.product_name

    @property
    def product(self):
        return self.purchase_product.product

    @property
    def batch(self):
        return self.purchase_product.batch_number

    @property
    def expiration_date(self):
        return self.purchase_product.expiration_date

    @property
    def stock_id(self):
        return self.purchase_product.stock_identifier


class PutAway(models.Model):
    status_choices = (
        ("Not Started", "Not Started"),
        ("In Process", "In Process"),
        ("Finished", "Finished"),
    )

    put_site = models.ForeignKey(
        "inventory.site", null=True, on_delete=models.SET_NULL
    )
    final_unload = models.ForeignKey(
        Unload, on_delete=models.CASCADE, null=True
    )
    status = models.CharField(
        choices=status_choices,
        max_length=15,
        null=True,
        blank=True,
        default="Not Started",
    )

    created_date = models.DateTimeField(auto_now_add=True)

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
    put_area = models.ForeignKey(
        "inventory.logisticarea", null=True, on_delete=models.SET_NULL
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unload_product.product_name

    @property
    def product(self):
        return self.unload_product.product

    @property
    def batch(self):
        return self.unload_product.batch

    @property
    def expiration_date(self):
        return self.unload_product.expiration_date

    @property
    def unload_qty(self):
        return self.unload_product.unload_qty

    @property
    def stock_id(self):
        return self.unload_product.stock_id

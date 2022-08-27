from django.db import models


class PurchaseOrder(models.Model):
    inbound_status_choices = (
        ("Ordered", "Ordered"),
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )

    supplier = models.ForeignKey("accounts.supplier", on_delete=models.CASCADE)
    inbound_status = models.CharField(
        max_length=50, choices=inbound_status_choices, verbose_name="Status"
    )
    facility = models.ForeignKey(
        "accounts.facility", on_delete=models.SET_NULL, null=True
    )
    discount = models.DecimalField(decimal_places=2, max_digits=4, default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    @property
    def reference_id(self):
        return f"PO-{self.pk}"

    def __str__(self):
        return self.reference_id


class PurchaseOrderProduct(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(
        "formulary.product_list", on_delete=models.CASCADE
    )
    supplied_qty = models.IntegerField()
    cost_price = models.FloatField()
    batch_nummber = models.CharField(max_length=225)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name


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
    status = models.CharField(choices=status_choices, max_length=100)
    purchase_product = models.ForeignKey(
        PurchaseOrderProduct, on_delete=models.CASCADE
    )
    unload_qty = models.IntegerField()

    def unload_return_qty(self):
        return self.purchase_product.supplied_qty - self.unload_qty

    def __str__(self):
        return self.site_id


class Put_Away(models.Model):
    status_choices = (
        ("Not Started", "Not Started"),
        ("In Process", "In Process"),
        ("Finished", "Finished"),
    )

    put_site = models.ForeignKey(
        "inventory.site", null=True, on_delete=models.SET_NULL
    )
    put_area = models.ForeignKey(
        "inventory.logisticarea", null=True, on_delete=models.SET_NULL
    )
    final_unload = models.ForeignKey(Unload, on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices, max_length=225)

    def __str__(self) -> str:
        return self.put_site

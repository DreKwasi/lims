from accounts.models import Facility
from django.db import models
from formulary.models import Product_List


class Site(models.Model):
    facility = models.OneToOneField(
        "accounts.facility", on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def site_id(self):
        return "SITE_" + self.facility.facility_name.lower().replace(" ", "_")

    def __str__(self):
        return self.site_id


class LogisticArea(models.Model):
    area_name = models.CharField(max_length=100, unique=True)
    area_description = models.CharField(max_length=100)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name


class Inventory(models.Model):

    stock_type_choices = (
        ("Warehouse", "Warehouse"),
        ("Pre-Delivered", "Pre-Delivered"),
        ("In-Transit", "In-Transit"),
    )

    stock_type = models.CharField(max_length=100, choices=stock_type_choices)
    product = models.ForeignKey(Product_List, on_delete=models.CASCADE)
    pack_quantity = models.IntegerField(verbose_name="Number of packs")
    site_id = models.ForeignKey(Site, null=True, on_delete=models.SET_NULL)

    expiration_date = models.DateTimeField()
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"

    def __str__(self):
        return self.product.product_name

    @property
    def unit_quantity(self):
        return self.product.uom * self.pack_quantity

import uuid

from accounts.models import Facility
from django.core.validators import MinValueValidator
from django.db import models
from formulary.models import ProductList


class Site(models.Model):
    facility = models.OneToOneField(
        "accounts.facility", on_delete=models.CASCADE, related_name="site"
    )
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def site_id(self):
        return "SITE_" + self.facility.facility_name.lower().replace(" ", "_")

    @property
    def facility_name(self):
        return self.facility.facility_name

    def __str__(self):
        return self.site_id


class LogisticArea(models.Model):
    area_name = models.CharField(max_length=100, unique=True)
    area_description = models.CharField(max_length=100)
    site_id = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name="areas"
    )

    def __str__(self):
        return self.area_name


class InventoryManager(models.Model):
    stock_type_choices = (
        ("Warehouse", "Warehouse"),
        ("Pre-Delivered", "Pre-Delivered"),
        ("In-Transit", "In-Transit"),
    )
    stock_type = models.CharField(max_length=100, choices=stock_type_choices)


class Inventory(models.Model):

    stock_type_choices = (
        ("Warehouse", "Warehouse"),
        ("Pre-Delivered", "Pre-Delivered"),
        ("In-Transit", "In-Transit"),
    )
    stock_type = models.CharField(max_length=100, choices=stock_type_choices)
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    batch = models.CharField(max_length=225, blank=True, null=True)
    pack_quantity = models.PositiveIntegerField(
        verbose_name="Number of packs", validators=[MinValueValidator(1)]
    )
    logistic_area = models.ForeignKey(
        "inventory.logisticarea",
        on_delete=models.SET_NULL,
        null=True,
        related_name="inventory_areas",
    )
    stock_identifier = models.UUIDField(default=uuid.uuid4, blank=True)
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

    @property
    def site_id(self):
        return self.logistic_area.site_id

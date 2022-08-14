from tabnanny import verbose
from django.db import models
from formulary.models import Product_List


class Inventory_Data(models.Model):
    stock_type_choices = (
        ("Warehouse", "Warehouse"),
        ("In-Transit", "In-Transit"),
        ("Delivered", "Delivered"),
    )

    stock_type = models.CharField(max_length=100, choices=stock_type_choices)


class Inventory(models.Model):
    product = models.ForeignKey(Product_List, on_delete=models.CASCADE)
    inventory_type = models.ForeignKey(
        Inventory_Data, on_delete=models.CASCADE
    )
    pack_quantity = models.IntegerField(verbose_name="Number of packs")

    @property
    def unit_quantity(self):
        return self.product.uom * self.pack_quantity

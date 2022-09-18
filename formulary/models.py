from django.db import models
from django.utils.translation import gettext_lazy as _


# Developing table classes for Formulary


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(
        max_length=100, null=True, unique=True
    )
    tier = models.CharField(max_length=100, null=True, unique=True)
    price_range = models.CharField(max_length=225, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manufacturer_name


class Form(models.Model):
    form = models.CharField(max_length=100, null=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.form


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, unique=True)
    description = models.TextField(max_length=225, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name


class ProductList(models.Model):

    # uom_choices = (
    #     ("pack", "pack(s)"),
    #     ("batch", "batch"),
    #     ("volume", "volume"),
    #     ("weight", "weight"),
    #     ("unit", "unit"),
    # )

    product_name = models.CharField(max_length=225, unique=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name="category_products",
    )

    product_form = models.ForeignKey(
        Form,
        null=True,
        on_delete=models.SET_NULL,
        related_name="form_products",
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        null=True,
        on_delete=models.SET_NULL,
        related_name="manufacturer_products",
    )

    # base_uom = models.CharField(choices=uom_choices)
    unit_of_measure = models.IntegerField(verbose_name=_("Pack Size"))
    details = models.TextField(max_length=225, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "accounts.Account",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_products",
    )

    def __str__(self):
        return self.product_name

    @property
    def product_id(self):
        return f"CHEM-{self.pk}"

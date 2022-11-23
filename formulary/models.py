import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Developing table classes for Formulary


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(
        max_length=100, null=True, unique=True
    )
    tier = models.CharField(max_length=100, null=True)
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

    details = models.TextField(max_length=225, blank=True, null=True)
    product_image = models.ImageField(
        upload_to="products", blank=True, null=True
    )
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


class UnitOfMeasure(models.Model):
    product = models.OneToOneField(
        ProductList,
        on_delete=models.CASCADE,
        related_name="product_uom",
        null=True,
        blank=True,
    )
    milliliter = models.IntegerField(
        verbose_name="Volume in Mls", null=True, blank=True
    )
    gram = models.IntegerField(
        verbose_name="Weight in Gram", null=True, blank=True
    )
    pack = models.IntegerField(
        verbose_name="Units Per Pack",
        null=True,
        blank=True,
    )
    unit = models.IntegerField(verbose_name="Unit", null=True, blank=True)

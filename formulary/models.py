from django.db import models


# Developing table classes for Formulary


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(
        max_length=100, null=True, unique=True
    )

    def __str__(self):
        return self.manufacturer_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.brand_name


class Generic_Attr(models.Model):
    generic_name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.generic_name


class Form(models.Model):
    brand_name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.brand_name


class Tier(models.Model):
    tier = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.tier


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=225, blank=True)


class Product_List(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=225, unique=True)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    product_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
    product_form = models.ForeignKey(Form, on_delete=models.SET_NULL)
    product_generic_name = models.ForeignKey(
        Generic_Attr, on_delete=models.SET_NULL
    )
    product_manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL
    )
    product_tier = models.ForeignKey(Tier, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_name

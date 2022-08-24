from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = (
        "category_name",
        "slug",
        "is_active",
        "created_date",
    )


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("manufacturer_name", "is_active", "created_date")


admin.site.register(Manufacturer, ManufacturerAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "is_active", "created_date")


admin.site.register(Brand, BrandAdmin)


class FormAdmin(admin.ModelAdmin):
    list_display = ("form", "is_active", "created_date")


admin.site.register(Form, FormAdmin)


class GenericAttrAdmin(admin.ModelAdmin):
    list_display = ("generic_name", "is_active", "created_date")


admin.site.register(Generic_Attr, GenericAttrAdmin)


class TierAdmin(admin.ModelAdmin):
    list_display = ("tier", "price_range", "is_active", "created_date")


admin.site.register(Tier, TierAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_category",
        "product_brand",
        "product_form",
        "unit_of_measure",
        "is_active",
        "created_date",
    )


admin.site.register(Product_List, ProductAdmin)

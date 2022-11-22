from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "category_name",
        "is_active",
        "created_date",
    )


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("manufacturer_name", "is_active", "created_date")


admin.site.register(Manufacturer, ManufacturerAdmin)


class FormAdmin(admin.ModelAdmin):
    list_display = ("form", "is_active", "created_date")


admin.site.register(Form, FormAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "category",
        "product_form",
        "product_uom",
        "is_active",
        "created_date",
    )
    list_editable = ("is_active",)


admin.site.register(ProductList, ProductAdmin)


class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ("product", "milliliter", "gram", "pack")


admin.site.register(UnitOfMeasure, UnitOfMeasureAdmin)

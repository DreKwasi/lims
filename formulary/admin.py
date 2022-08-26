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


class GenericAttrAdmin(admin.ModelAdmin):
    list_display = ("generic_name", "is_active", "created_date")


admin.site.register(Generic_Attr, GenericAttrAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "category",
        "product_form",
        "unit_of_measure",
        "is_active",
        "created_date",
    )


admin.site.register(Product_List, ProductAdmin)

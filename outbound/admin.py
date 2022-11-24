from django.contrib import admin

from .models import *


class StockTransferAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "ship_to_location",
        "ship_from_location",
        "order_priority",
        "status",
        "created_date",
        "updated_date",
    ]


admin.site.register(StockTransfer, StockTransferAdmin)


class StockTransferProductAdmin(admin.ModelAdmin):
    list_display = [
        "stock_transfer_order",
        "product",
        "inventory_level",
        "quantity",
        "unit_of_measure",
        "status",
        "created_date",
        "updated_date",
    ]


admin.site.register(StockTransferProduct, StockTransferProductAdmin)


class PickPackAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "ship_to_location",
        "ship_from_location",
        "status",
        "user",
        "created_date",
        "updated_date",
    ]


admin.site.register(PickPack, PickPackAdmin)


class PickPackProductAdmin(admin.ModelAdmin):
    list_display = [
        "pickpack",
        "product",
        "quantity",
        "batch_number",
        "expiration_date",
        "created_date",
        "updated_date",
    ]


admin.site.register(PickPackProduct, PickPackProductAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "ship_to_location",
        "ship_from_location",
        "status",
        "user",
        "created_date",
        "updated_date",
    ]


admin.site.register(Delivery, DeliveryAdmin)


class DeliveryProductAdmin(admin.ModelAdmin):
    list_display = [
        "delivery",
        "product",
        "quantity",
        "batch_number",
        "expiration_date",
        "created_date",
        "updated_date",
    ]


admin.site.register(DeliveryProduct, DeliveryProductAdmin)

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


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = [
        "account",
        "order_priority",
        "status",
        "created_date",
        "updated_date",
    ]


admin.site.register(SalesOrder, SalesOrderAdmin)


class SalesOrderProductAdmin(admin.ModelAdmin):
    list_display = [
        "sales_order",
        "product",
        "inventory_level",
        "quantity",
        "unit_of_measure",
        "status",
    ]


admin.site.register(SalesOrderProduct, SalesOrderProductAdmin)

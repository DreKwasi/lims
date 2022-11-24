from django.contrib import admin

from .models import *


class SiteAdmin(admin.ModelAdmin):
    list_display = (
        "site_id",
        "facility",
    )


class LogisticAreaAdmin(admin.ModelAdmin):
    list_display = (
        "area_name",
        "site_id",
    )


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "pack_quantity",
        "logistic_area",
        "stock_identifier",
        "expiration_date",
        "created_date",
    )
    list_filter = (
        "product",
        "logistic_area",
        "expiration_date",
        "stock_identifier",
    )


admin.site.register(Site, SiteAdmin)
admin.site.register(LogisticArea, LogisticAreaAdmin)
admin.site.register(Inventory, InventoryAdmin)

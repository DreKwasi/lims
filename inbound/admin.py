from django.contrib import admin
from .models import *


class PurchaseOrderProductAdmin(admin.ModelAdmin):
    list_display = [
        "purchase_order",
        "product",
        "batch_number",
        "expiration_date",
        "created_date",
        "stock_identifier",
    ]


class PurchaseOrderProductInline(admin.TabularInline):
    model = PurchaseOrderProduct


admin.site.register(PurchaseOrderProduct, PurchaseOrderProductAdmin)


class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseOrderProductInline,
    ]
    list_display = [
        "purchase_order_id",
        "supplier",
        "order_status",
        "facility",
        "created_date",
    ]
    raw_id_fields = [
        "supplier",
        "facility",
    ]
    list_filter = [
        "supplier",
        "facility",
        "order_status",
    ]


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class UnloadAdmin(admin.ModelAdmin):
    list_display = [
        "unload_id",
        "purchase_order",
        "site_id",
        "status",
        "created_date",
    ]
    list_editable = ["status"]


admin.site.register(Unload, UnloadAdmin)


class UnloadProductAdmin(admin.ModelAdmin):
    list_display = [
        "unload",
        "purchase_product",
        "unload_qty",
        "created_date",
    ]


admin.site.register(UnloadProduct, UnloadProductAdmin)


class PutAwayAdmin(admin.ModelAdmin):
    list_display = [
        "final_unload",
        "put_site",
        "status",
        "created_date",
    ]
    list_editable = ["status"]


admin.site.register(PutAway, PutAwayAdmin)


class PutAwayProductAdmin(admin.ModelAdmin):
    list_display = [
        "putaway",
        "unload_product",
        "put_area",
        "created_date",
    ]


admin.site.register(PutAwayProduct, PutAwayProductAdmin)

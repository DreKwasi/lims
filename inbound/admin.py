from django.contrib import admin

from .models import *


class PurchaseOrderProductAdmin(admin.ModelAdmin):
    list_display = [
        "purchase_order",
        "product",
        "open_quantity",
        "delivered_quantity",
        "created_date",
        "updated_date",
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
        "payment_terms",
        "facility",
        "created_date",
        "actual_delivery_date",
    ]
    raw_id_fields = [
        "supplier",
        "facility",
    ]
    list_filter = ["supplier", "facility", "order_status", "payment_terms"]


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


admin.site.register(PurchaseOrderTransaction)


class IdentifiedStockInline(admin.TabularInline):
    model = IdentifiedStock


class IdentifiedStockAdmin(admin.ModelAdmin):
    list_display = [
        "batch_number",
        "stock_identifier",
        "unload",
    ]


admin.site.register(IdentifiedStock, IdentifiedStockAdmin)


class UnloadProductAdmin(admin.ModelAdmin):
    inlines = [IdentifiedStockInline]
    list_display = [
        "unload",
        "purchase_product",
        "open_quantity",
        "actual_quantity",
    ]


class UnloadProductInline(admin.TabularInline):
    model = UnloadProduct


admin.site.register(UnloadProduct, UnloadProductAdmin)


class UnloadAdmin(admin.ModelAdmin):
    inlines = [UnloadProductInline]
    list_display = [
        "unload_id",
        "target_logistic_area",
        "purchase_order",
        "site_id",
        "status",
        "created_date",
    ]
    list_editable = ["status"]


admin.site.register(Unload, UnloadAdmin)


class PutAwayProductAdmin(admin.ModelAdmin):
    list_display = [
        "putaway",
        "unload_product",
        "target_logistic_area",
        "open_quantity",
        "actual_quantity",
        "batch",
        "stock_identifier",
    ]


class PutAwayProductInline(admin.TabularInline):
    model = PutAwayProduct


admin.site.register(PutAwayProduct, PutAwayProductAdmin)


class PutAwayAdmin(admin.ModelAdmin):
    inlines = [PutAwayProductInline]
    list_display = [
        "put_away_id",
        "final_unload",
        "site_id",
        "source_logistic_area",
        "status",
        "created_date",
    ]
    list_editable = ["status"]


admin.site.register(PutAway, PutAwayAdmin)

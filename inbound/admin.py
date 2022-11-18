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
    extra = 0


admin.site.register(PurchaseOrderProduct, PurchaseOrderProductAdmin)


class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseOrderProductInline,
    ]
    list_display = [
        "__str__",
        "supplier",
        "order_status",
        "payment_terms",
        "facility",
        "created_date",
        "due_date",
    ]
    list_editable = [
        "order_status",
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
    extra = 0


class IdentifiedStockAdmin(admin.ModelAdmin):
    list_display = [
        "batch_number",
        "stock_identifier",
        "unload_product",
        "unload",
    ]


admin.site.register(IdentifiedStock, IdentifiedStockAdmin)


class UnloadProductAdmin(admin.ModelAdmin):
    inlines = [IdentifiedStockInline]
    list_display = [
        "unload",
        "product",
        "open_quantity",
        "actual_quantity",
    ]


class UnloadProductInline(admin.TabularInline):
    model = UnloadProduct
    extra = 0


admin.site.register(UnloadProduct, UnloadProductAdmin)


class UnloadAdmin(admin.ModelAdmin):
    inlines = [UnloadProductInline]
    list_display = [
        "unload_id",
        "purchase_order",
        "site_id",
        "status",
        "created_date",
    ]
    list_editable = ["status"]


admin.site.register(Unload, UnloadAdmin)

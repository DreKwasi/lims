import django_filters

from .models import *


class PurchaseOrderFilter(django_filters.FilterSet):

    supplier = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = PurchaseOrder
        fields = ["supplier", "reference_id", "order_status", "created_date"]


class PurchaseProductFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(
        field_name="product__product_name", lookup_expr="icontains"
    )

    class Meta:
        model = PurchaseOrderProduct
        fields = "__all__"


class UnloadProductFilter(django_filters.FilterSet):
    unload = django_filters.CharFilter(
        field_name="unload__id", lookup_expr="icontains"
    )

    class Meta:
        model = UnloadProduct
        fields = "__all__"


class IdentifiedStockFilter(django_filters.FilterSet):
    unload = django_filters.CharFilter(
        field_name="unload__id", lookup_expr="icontains"
    )
    unload_product = django_filters.CharFilter(
        field_name="unload_product__product", lookup_expr="icontains"
    )

    class Meta:
        model = IdentifiedStock
        fields = "__all__"

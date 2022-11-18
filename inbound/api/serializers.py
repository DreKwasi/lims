
from rest_framework import serializers

from accounts.models import Facility, Supplier
from formulary.models import ProductList
from inbound.models import (
    IdentifiedStock,
    PurchaseOrder,
    PurchaseOrderProduct,
    Unload,
    UnloadProduct,
)
from inventory.models import LogisticArea, Site


class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(
        slug_field="supplier_name",
        queryset=Supplier.objects.all(),
        required=False,
    )
    facility = serializers.SlugRelatedField(
        slug_field="facility_name",
        queryset=Facility.objects.all(),
        required=False,
    )
    order_date = serializers.DateField(format="%Y-%m-%d", required=False)
    total_value = serializers.ReadOnlyField()

    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "supplier",
            "facility",
            "reference_id",
            "order_status",
            "order_date",
            "total_value",
            "due_date",
            "payment_terms",
        ]


class PurchaseProductSerializer(serializers.ModelSerializer):
    purchase_order = serializers.PrimaryKeyRelatedField(
        queryset=PurchaseOrder.objects.all(),
        required=False,
    )
    product = serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=ProductList.objects.all(),
    )

    class Meta:
        model = PurchaseOrderProduct
        fields = [
            "id",
            "open_quantity",
            "planned_quantity",
            "delivered_quantity",
            "unit_price",
            "discount",
            "purchase_order",
            "product",
            "total_value",
        ]


class UnloadSerializer(serializers.ModelSerializer):
    purchase_order = serializers.SlugRelatedField(
        slug_field="id",
        queryset=PurchaseOrder.objects.all(),
        required=False,
    )
    site_id = serializers.SlugRelatedField(
        slug_field="facility_name",
        queryset=Site.objects.all(),
        required=False,
    )

    created_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Unload
        fields = [
            "id",
            "unload_id",
            "purchase_order",
            "status",
            "site_id",
            "created_date",
        ]


class IdentifiedStockSerializer(serializers.ModelSerializer):
    unload_product = serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=UnloadProduct.objects.all(),
        required=False,
    )
    created_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    target_logistic_area = serializers.SlugRelatedField(
        slug_field="area_name",
        queryset=LogisticArea.objects.all(),
        required=False,
    )

    # unload_product = UnloadProductSerializer()

    class Meta:
        model = IdentifiedStock
        fields = [
            "batch_number",
            "expiration_date",
            "target_logistic_area",
            "unload_id",
            "stock_identifier",
            "unload_product",
            "split_quantity",
            "created_date",
        ]


class UnloadProductSerializer(serializers.ModelSerializer):
    unload = serializers.SlugRelatedField(
        slug_field="unload_id", queryset=Unload.objects.all(), required=False
    )
    product = serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=ProductList.objects.all(),
        required=False,
    )
    created_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    identified_stock = IdentifiedStockSerializer(many=True)

    class Meta:
        model = UnloadProduct
        fields = [
            "unload",
            "product",
            "open_quantity",
            "planned_quantity",
            "actual_quantity",
            "created_date",
            "identified_stock",
        ]

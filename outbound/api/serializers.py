from rest_framework import serializers

from formulary.models import ProductList

from ..models import StockTransfer, StockTransferProduct


class StockTransferProductSerializer(serializers.Serializer):
    stock_transfer = serializers.SlugRelatedField(
        slug_field="__str__",
        queryset=StockTransfer.objects.all(),
        required=False,
    )
    product = serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=ProductList.objects.all(),
        required=False,
    )

    class Meta:
        model = StockTransferProduct
        fields = [
            "stock_transfer",
            "product",
            "status",
            "unit_of_measure",
            "quantity",
            "inventory_level",
            "created_date",
            "updated_date",
        ]


class StockTransferSerializer(serializers.ModelSerializer):
    stock_transfer_products = StockTransferProductSerializer(many=True)

    class Meta:
        model = StockTransfer
        fields = [
            "__str__",
            "ship_to_location",
            "ship_from_location",
            "status",
            "order_priority",
            "user",
            "created_date",
            "updated_date",
        ]

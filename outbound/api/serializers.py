from rest_framework import serializers

from accounts.models import Account, Facility
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
    status = serializers.ChoiceField(
        choices=[
            "Released",
            "Not Started" "Cancelled",
            "Not Released",
            "Partial",
            "Delivered",
        ]
    )
    unit_of_measure = serializers.ChoiceField(
        choices=["Packs", "Units", "Volume in Mls", "Weight in Grams"]
    )
    quantity = serializers.IntegerField()
    inventory_level = serializers.IntegerField()
    created_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    updated_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

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
    stock_transfer_products = StockTransferProductSerializer(
        many=True, read_only=True
    )
    ship_to_location = serializers.SlugRelatedField(
        queryset=Facility.objects.all(), slug_field="facility_name"
    )
    ship_from_location = serializers.SlugRelatedField(
        queryset=Facility.objects.all(), slug_field="facility_name"
    )
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=Account.objects.all()
    )
    created_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    updated_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = StockTransfer
        fields = [
            "id",
            "stock_transfer_id",
            "stock_transfer_products",
            "ship_to_location",
            "ship_from_location",
            "status",
            "order_priority",
            "user",
            "created_date",
            "updated_date",
        ]

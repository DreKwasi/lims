from rest_framework import serializers

from accounts.api.serializers import AccountSerializer
from formulary.models import *


class CategorySerializer(serializers.ModelSerializer):
    category_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="products-detail",
    )
    category_name = serializers.CharField(required=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        model = Category
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    manufacturer_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="products-detail",
    )

    manufacturer_name = serializers.CharField(required=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductFormSerializer(serializers.ModelSerializer):
    form_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="products-detail",
    )

    form = serializers.CharField(required=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        model = Form
        fields = "__all__"


class UnitOfMeasureSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=ProductList.objects.all(),
        slug_field="product_name",
        read_only=False,
        required=False,
    )

    class Meta:
        model = UnitOfMeasure
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField()
    created_by = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="category_name"
    )

    manufacturer = serializers.SlugRelatedField(
        slug_field="manufacturer_name",
        queryset=Manufacturer.objects.all(),
        read_only=False,
    )
    product_form = serializers.SlugRelatedField(
        slug_field="form", queryset=Form.objects.all(), read_only=False
    )
    product_uom = UnitOfMeasureSerializer(read_only=True, many=False)

    class Meta:
        model = ProductList
        fields = "__all__"

    def create(self, validated_data):
        request = self.context["request"]
        return ProductList.objects.create(
            created_by=request.user, **validated_data
        )

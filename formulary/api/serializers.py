from accounts.api.serializers import AccountSerializer
from formulary.models import *
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    category = serializers.SlugRelatedField(
        slug_field="category_name",
        queryset=Category.objects.all(),
        read_only=False,
    )
    manufacturer = serializers.SlugRelatedField(
        slug_field="manufacturer_name",
        queryset=Manufacturer.objects.all(),
        read_only=False,
    )
    product_form = serializers.SlugRelatedField(
        slug_field="form", queryset=Form.objects.all(), read_only=False
    )

    class Meta:
        model = ProductList
        fields = "__all__"

    def create(self, validated_data):
        request = self.context["request"]
        return ProductList.objects.create(
            created_by=request.user, **validated_data
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer


class ProductFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form

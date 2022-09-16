from accounts.api.serializers import AccountSerializer
from formulary.models import *
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )
    category = serializers.SlugRelatedField(
        slug_field="category_name",
        queryset=Category.objects.all(),
        read_only=False,
    )
    manufacturer = serializers.SlugRelatedField(
        slug_field="manufacturer_name", read_only=True
    )
    product_form = serializers.SlugRelatedField(
        slug_field="form", read_only=True
    )

    class Meta:
        model = ProductList
        fields = "__all__"

import django_filters

from .models import Product_List


class ProductFilter(django_filters.FilterSet):
    category__category_name = django_filters.CharFilter(
        field_name="category__category_name", lookup_expr="icontains"
    )

    manufacturer__manufacturer_name = django_filters.CharFilter(
        field_name="manufacturer__manufacturer_name",
        lookup_expr="icontains",
    )

    product_form__form = django_filters.CharFilter(
        field_name="product_form__form",
        lookup_expr="icontains",
    )

    class Meta:
        model = Product_List
        fields = [
            "product_id",
            "category__category_name",
            "product_form__form",
            "manufacturer__manufacturer_name",
        ]

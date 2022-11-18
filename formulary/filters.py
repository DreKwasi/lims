import django_filters
from django_filters import filters
from rest_framework_datatables.django_filters.filters import GlobalFilter
from rest_framework_datatables.django_filters.filterset import (
    DatatablesFilterSet,
)

from .models import *


class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass


class ProductDatatableFilterSet(DatatablesFilterSet):

    product_name = GlobalCharFilter(lookup_expr="icontains")
    manufacturer = GlobalCharFilter(
        field_name="manufacturer__manufacturer_name", lookup_expr="icontains"
    )

    product_form = GlobalCharFilter(
        field_name="product_form__form", lookup_expr="icontains"
    )

    category = GlobalCharFilter(
        field_name="category__category_name", lookup_expr="icontains"
    )

    class Meta:
        model = ProductList
        fields = [
            "product_name",
            "manufacturer",
            "product_form",
            "category",
        ]


class ProductListFilterSet(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ProductList
        fields = [
            "product_name",
        ]



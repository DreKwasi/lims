import django_filters
from accounts.models import Facility, Supplier


class SupplierFilterSet(django_filters.FilterSet):

    supplier_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Supplier
        fields = "__all__"


class FacilityFilterSet(django_filters.FilterSet):
    facility_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Facility
        fields = "__all__"

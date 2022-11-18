import django_filters
from .models import Site, LogisticArea, Inventory


class SiteFilterSet(django_filters.FilterSet):
    facility = django_filters.CharFilter(
        field_name="facility__facility_name", lookup_expr="icontains"
    )

    class Meta:
        model = Site
        fields = "__all__"


class LogisticAreaFilterSet(django_filters.FilterSet):
    class Meta:
        model = LogisticArea
        fields = "__all__"

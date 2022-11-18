from accounts.models import Facility, Supplier
from rest_framework import generics, mixins, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SupplierFilterSet, FacilityFilterSet
from .serializers import FacilitySerializer, SupplierSerializer


class CreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class SupplierApiViewset(CreateListRetrieveViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    lookup_field = "supplier_name"
    filterset_class = SupplierFilterSet
    filterset_field = "supplier_name"


class FacilityApiViewset(CreateListRetrieveViewSet):
    serializer_class = FacilitySerializer
    queryset = Facility.objects.all()
    filter_backends = [DjangoFilterBackend]
    lookup_field = "facility_name"
    filterset_class = FacilityFilterSet
    filterset_field = "facility_name"
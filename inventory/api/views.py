from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from inventory.filters import LogisticAreaFilterSet, SiteFilterSet
from inventory.models import Inventory, LogisticArea, Site

from .serializers import LogisticAreaSerializer, SiteSerializer


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


class SiteViewSet(CreateListRetrieveViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backend = DjangoFilterBackend
    filterset_class = SiteFilterSet


class LogisticAreaViewSet(CreateListRetrieveViewSet):
    queryset = LogisticArea.objects.all()
    serializer_class = LogisticAreaSerializer
    filter_backend = DjangoFilterBackend
    filterset_class = LogisticAreaFilterSet

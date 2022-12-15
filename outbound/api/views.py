from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from .serializers import (
    StockTransferSerializer,
    StockTransferProductSerializer,
)
from ..models import StockTransfer, StockTransferProduct


# Viewset for Models that Can be Created But Not Destroyed
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


# Viewset for Models that Accept Only Updates eg: PickPack and Delivery
class UpdateListRetrieveViewSet(
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


class StockTransferApiViewSet(CreateListRetrieveViewSet):
    serializer_class = StockTransferSerializer #serializer_class of Viewset to serialize json requests
    queryset = StockTransfer.objects.all() #queryset for defining which model the Viewset will query

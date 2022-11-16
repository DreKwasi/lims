from functools import partial

from accounts.models import Account
from formulary.models import Category, Form, Manufacturer, ProductList
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    ManufacturerSerializer,
    ProductFormSerializer,
    ProductListSerializer,
)


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


class ProductListApiViewset(CreateListRetrieveViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CategoryApiViewset(CreateListRetrieveViewSet):
    queryset = Category.objects.prefetch_related("category_products")
    serializer_class = CategorySerializer


class FormApiViewset(CreateListRetrieveViewSet):
    queryset = Form.objects.all()
    serializer_class = ProductFormSerializer


class ManApiViewset(CreateListRetrieveViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

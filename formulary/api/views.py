from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from accounts.models import Account
from formulary.filters import UnitOfMeasureFilterSet
from formulary.models import (
    Category,
    Form,
    Manufacturer,
    ProductList,
    UnitOfMeasure,
)

from .serializers import (
    CategorySerializer,
    ManufacturerSerializer,
    ProductFormSerializer,
    ProductListSerializer,
    UnitOfMeasureSerializer,
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


class UnitOfMeasureApiViewset(CreateListRetrieveViewSet):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer
    filter_backend = DjangoFilterBackend
    filterset_class = UnitOfMeasureFilterSet

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            print("Valid")
            serializer.save(
                product=ProductList.objects.get(
                    product_name=request.data.get("product")
                )
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("not Valid")
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        uom = self.get_object()
        serializer = self.serializer_class(uom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CategoryApiViewset(CreateListRetrieveViewSet):
    queryset = Category.objects.prefetch_related("category_products")
    serializer_class = CategorySerializer


class FormApiViewset(CreateListRetrieveViewSet):
    queryset = Form.objects.all()
    serializer_class = ProductFormSerializer


class ManApiViewset(CreateListRetrieveViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

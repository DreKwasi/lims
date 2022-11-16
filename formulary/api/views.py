from django_filters.rest_framework import DjangoFilterBackend
from formulary.filters import ProductDatatableFilterSet, ProductListFilterSet
from formulary.models import Category, Form, Manufacturer, ProductList
from rest_framework import generics, mixins, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework_datatables.django_filters import backends

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


class ProductListApiViewset(
    CreateListRetrieveViewSet, generics.GenericAPIView
):
    queryset = ProductList.objects.all().order_by("created_date")
    serializer_class = ProductListSerializer
    parser_classes = (
        FormParser,
        MultiPartParser,
    )
    filter_backend = DjangoFilterBackend
    filterset_class = ProductListFilterSet
    filterset_field = "product_name"

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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

from formulary.models import ProductList
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProductListSerializer


class ProductListApiView(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = ProductList.objects.all()
    # permission_classes = [IsAuthenticated]

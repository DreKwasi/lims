from django.urls import include, path
from rest_framework import routers

from .views import (
    IdentifiedStockApiViewset,
    PurchaseOrderApiViewset,
    PurchaseProductApiViewset,
    UnloadApiViewset,
    UnloadProductApiViewset,
)

router = routers.DefaultRouter()

router.register(
    r"purchase_orders",
    PurchaseOrderApiViewset,
    basename="purchase_order",
)

router.register(
    r"purchase_products",
    PurchaseProductApiViewset,
    basename="purchase_products",
)

router.register(r"unloads", UnloadApiViewset, basename="unloads")
router.register(
    r"unload_products", UnloadProductApiViewset, basename="unload_products"
)
router.register(
    r"identified_stock", IdentifiedStockApiViewset, basename="identified_stock"
)

urlpatterns = [path("", include(router.urls))]

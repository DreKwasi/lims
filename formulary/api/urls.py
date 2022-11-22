from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryApiViewset,
    FormApiViewset,
    ManApiViewset,
    ProductListApiViewset,
    UnitOfMeasureApiViewset,
)

router = DefaultRouter()

router.register(r"products", ProductListApiViewset, basename="products")
router.register(r"uom", UnitOfMeasureApiViewset, basename="uom")

router.register(
    r"product_category", CategoryApiViewset, basename="product_category"
)
router.register(r"product_form", FormApiViewset, basename="product_form")
router.register(
    r"product_manufacturer", ManApiViewset, basename="product_manufacturer"
)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls")),
]

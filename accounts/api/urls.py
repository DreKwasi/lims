from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FacilityApiViewset, SupplierApiViewset

router = DefaultRouter()

router.register(r"suppliers", SupplierApiViewset, basename="suppliers")
router.register(r"facilities", FacilityApiViewset, basename="facilities")

urlpatterns = [path("", include(router.urls))]

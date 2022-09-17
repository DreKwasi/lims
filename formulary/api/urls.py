from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r"products", ProductListApiViewset, basename="products")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls")),
]

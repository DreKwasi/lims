from django.urls import path, include
from rest_framework import routers
from .views import LogisticAreaViewSet, SiteViewSet

router = routers.DefaultRouter()

router.register(
    r"logistic_areas", LogisticAreaViewSet, basename="logistic_areas"
)
router.register(r"site", SiteViewSet, basename="site")

urlpatterns = [path("", include(router.urls))]

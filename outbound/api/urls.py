from django.urls import include, path #modules for managing django url routing
from rest_framework.routers import DefaultRouter  # handling api routes
from .views import StockTransferApiViewSet  # import needed viewset for routing

router = DefaultRouter() #Initialize DefaultRouter object to a variable

# Register required API Routes to Viewsets
router.register(
    r"stock_transfers", StockTransferApiViewSet, basename="stock_transfers"
)

# Include API routes to DjangoUrl Routing
urlpatterns = [path("", include(router.urls))]

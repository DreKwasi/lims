import django_filters
from .models import *


class PurchaseOrderForm(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrder
        fields = ["supplier", "reference_id", "order_status", "created_date"]

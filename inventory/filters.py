from dataclasses import field
import django_filters
from .models import *


class InventoryFilter(django_filters.FilterSet):
    """_summary_

    Args:
        django_filters (_type_): _description_
    """

    class Meta:
        model = Inventory
        fields = "__all__"

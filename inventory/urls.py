from django.urls import path
from . import views

urlpatterns = [
    path("", views.inventory, name="inventory"),
    path("warehouse", views.warehouse, name="warehouse"),
    path("stock_transfer", views.stock_transfer, name="stock_transfer"),
    path("add_warehouse", views.add_warehouse, name="add_warehouse"),
]

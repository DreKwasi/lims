from django.urls import path

from . import views

urlpatterns = [
    path("", views.purchase_orders, name="purchase_orders"),
    path(
        "purchase_orders_data/",
        views.ajax_purchase_order_list_view,
        name="purchase_orders_data",
    ),
    path(
        "add_purchase_order/",
        views.add_purchase_order,
        name="add_purchase_order",
    ),
    path(
        "add_purchase_order/add_supplier/",
        views.add_supplier_modal,
        name="add_supplier",
    ),
    path(
        "add_purchase_order/get_supplier/",
        views.get_supplier,
        name="get_supplier",
    ),
]

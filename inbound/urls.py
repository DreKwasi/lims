from django.urls import path
from . import views


urlpatterns = [
    path("", views.purchase_orders, name="purchase_orders"),
    path("add_purchase/", views.add_purchase, name="add_purchase"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.formulary_view, name="formulary"),
    path("product_attr/", views.product_attr, name="product_attr"),
    path(
        "product_detail/<int:product_id>",
        views.product_detail,
        name="product_detail",
    ),
    path("add_product/", views.add_product, name="add_product"),
    path(
        "add_product_attr/<str:item>",
        views.add_product_attr,
        name="add_product_attr",
    ),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.formulary_view, name="formulary"),
    path(
        "product_detail/<int:product_id>",
        views.product_detail,
        name="product_detail",
    ),
]

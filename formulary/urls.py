from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="formulary/formulary_view.html"),
        name="formulary",
    ),
    path(
        "product_report/",
        TemplateView.as_view(template_name="formulary/product_report.html"),
        name="product_report",
    ),
    path(
        "product_detail/<int:product_id>",
        TemplateView.as_view(template_name="formulary/product_detail.html"),
        name="product_detail",
    ),
    path(
        "add_product/",
        TemplateView.as_view(template_name="formulary/add_product.html"),
        name="add_product",
    ),
    # path(
    #     "add_product_attr/<str:item>",
    #     TemplateView.as_view(template_name="formulary/product_report.html"),
    #     name="product_report",
    # ),
]

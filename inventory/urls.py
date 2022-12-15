from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="inventory/inventory.html"),
        name="inventory",
    ),
    path(
        "warehouse/",
        TemplateView.as_view(template_name="inventory/add_warehouse.html"),
        name="warehouse",
    ),
    path(
        "add_warehouse/",
        TemplateView.as_view(template_name="inventory/add_warehouse.html"),
        name="add_warehouse",
    ),
]

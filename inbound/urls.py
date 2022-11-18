from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="inbound/purchase_orders.html"),
        name="purchase_orders",
    ),
    path(
        "add_purchase_order/",
        TemplateView.as_view(template_name="inbound/add_purchase_order.html"),
        name="add_purchase_order",
    ),
    path(
        "preview_purchase_order/<int:pk>",
        TemplateView.as_view(
            template_name="inbound/print_preview_purchase_order.html"
        ),
        name="preview_purchase_order",
    ),
    path(
        "edit_purchase_order/<int:pk>",
        TemplateView.as_view(template_name="inbound/edit_purchase_order.html"),
        name="edit_purchase_order",
    ),
    path(
        "unload_tasks/",
        TemplateView.as_view(template_name="inbound/tasks.html"),
        name="unload_tasks",
    ),
    path(
        "preview_unload/<int:pk>",
        TemplateView.as_view(
            template_name="inbound/print_preview_unload.html"
        ),
        name="preview_unload",
    ),
    path(
        "edit_unload/<int:pk>",
        TemplateView.as_view(template_name="inbound/edit_unload.html"),
        name="edit_unload",
    ),
]

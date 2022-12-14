from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="outbound/stock_transfer.html"),
        name="stock_transfers",
    ),
    path(
        "new_stock_transfer",
        TemplateView.as_view(template_name="outbound/new_stock_transfer.html"),
        name="new_stock_transfer",
    ),
    path(
        "edit_stock_transfer",
        TemplateView.as_view(
            template_name="outbound/edit_stock_transfer.html"
        ),
        name="edit_stock_transfer",
    ),
]

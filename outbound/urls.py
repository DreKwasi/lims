from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "stock_transfers/",
        TemplateView.as_view(template_name="outbound/stock_transfers.html"),
        name="stock_transfers",
    ),
    path(
        "new_stock_transfer/",
        TemplateView.as_view(template_name="outbound/new_stock_transfer.html"),
        name="add_stock_transfer",
    ),
    path(
        "edit_stock_transfer/",
        TemplateView.as_view(
            template_name="outbound/edit_stock_transfer.html"
        ),
        name="edit_stock_transfer",
    ),
]

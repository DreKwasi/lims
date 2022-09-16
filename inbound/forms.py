from accounts.models import Facility, Supplier
from django import forms
from formulary.models import ProductList

from .models import *


class DateInput(forms.DateInput):
    input_type = "date"


class PurchaseOrderForm(forms.ModelForm):

    reference_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Reference #",
                "name": "refer",
            }
        ),
    )

    order_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control required editdate",
                "placeholder": "Billing Date",
                "type": "date",
            }
        ),
    )

    purchase_order_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "value": "{{new_order.purchase_order_id}}",
                "readonly": True,
            }
        ),
    )

    class Meta:
        model = PurchaseOrder
        fields = ["reference_id", "order_date", "purchase_order_id"]


class PurchaseOrderProductForm(forms.ModelForm):

    batch_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control product-form",
                "placeholder": " Batch #",
                "name": "batch",
            }
        ),
    )

    expiration_date = forms.DateField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control required editdate product-form",
                "placeholder": "Expiry Date",
                "type": "date",
            }
        ),
    )

    supplied_qty = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control product-form",
                "onkeypress": "return isNumber(event)",
            }
        ),
    )

    cost_price = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control product-form",
                "onkeypress": "return isNumber(event)",
            }
        ),
    )
    discount = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control product-form",
                "value": "0.0",
                "onkeypress": "return isNumber(event)",
            }
        ),
    )

    class Meta:
        model = PurchaseOrderProduct
        fields = "__all__"
        exclude = [
            "product",
            "purchase_order",
        ]

from accounts.models import Account
from django import forms

from .models import *


class ProductListForm(forms.ModelForm):
    product_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control margin-bottom  required"}
        )
    )

    product_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom  required",
                "readonly": True,
            },
        ),
    )

    unit_of_measure = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom  required",
                "onkeypress": "return isNumber(event)",
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Choose Category",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        empty_label="Choose Manufacturer",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    product_form = forms.ModelChoiceField(
        queryset=Form.objects.all(),
        empty_label="Choose Form",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    generic_name = forms.ModelChoiceField(
        queryset=Generic_Attr.objects.all(),
        empty_label="Choose Generic Name",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    created_by = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={"class": "form-control", "readonly": True}),
    )

    class Meta:
        model = Product_List
        fields = "__all__"

    def __init__(self, user, *args, **kwargs):
        super(ProductListForm, self).__init__(*args, **kwargs)
        self.fields["created_by"].queryset = Account.objects.filter(pk=user.id)

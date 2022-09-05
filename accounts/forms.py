from django import forms

from .models import Facility, Supplier


class SupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_name",
                "placeholder": "Name",
                "required": "true",
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_address",
                "placeholder": "Address",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_phone",
                "placeholder": "Phone Number",
            }
        )
    )
    contact_person = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_contact_person",
                "placeholder": "Contact Person",
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_email",
                "placeholder": "Email",
            }
        )
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_city",
                "placeholder": "City",
            }
        )
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_country",
                "placeholder": "Country",
            }
        )
    )
    postbox = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_postbox",
                "placeholder": "Post Box",
            }
        ),
    )
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom",
                "id": "msupplier_region",
                "placeholder": "Region",
            }
        )
    )

    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["phone_regex", "created_date", "created_by", "is_active"]

from accounts.models import Account
from django import forms

from .models import *


class ProductListForm(forms.ModelForm):
    product_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control margin-bottom  required"}
        )
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

    product_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control margin-bottom  required",
                "readonly": True,
            },
        ),
    )

    def __init__(self, user, *args, **kwargs):
        instance = kwargs.get("instance", None)
        if instance:
            kwargs["initial"] = {
                "product_id": instance.product_id,
            }
        super(ProductListForm, self).__init__(*args, **kwargs)
        self.fields["created_by"].queryset = Account.objects.filter(pk=user.id)
        self.fields["product_id"].required = False


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ("is_active",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control margin-bottom  required"

            self.fields[field].widget.attrs[
                "placeholder"
            ] = f"Enter {field} here ..."


class Manform(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
        exclude = ("is_active",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control margin-bottom  required"

            self.fields[field].widget.attrs[
                "placeholder"
            ] = f"Enter {field} here ..."


class ProductForm_Form(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
        exclude = ("is_active",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control margin-bottom  required"

            self.fields[field].widget.attrs[
                "placeholder"
            ] = f"Enter {field} here ..."


class GenericAttrForm(forms.ModelForm):
    class Meta:
        model = Generic_Attr
        fields = "__all__"
        exclude = ("is_active",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control margin-bottom  required"

            self.fields[field].widget.attrs[
                "placeholder"
            ] = f"Enter {field} here ..."


form_dict = {
    "category": CategoryForm,
    "manufacturer": Manform,
    "generic_name": GenericAttrForm,
    "product_form": ProductForm_Form,
}

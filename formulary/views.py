from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse

from .filters import ManufacturerFilter, ProductFilter
from .forms import *
from .models import *


def formulary_view(request):
    products = Product_List.objects.all()
    product_filter = ProductFilter(request.GET, products)
    context = {
        "product_filter": product_filter,
    }
    return render(request, "formulary/formulary_view.html", context)


def product_attr(request):
    manufacturers = Manufacturer.objects.all()
    man_filter = ManufacturerFilter(request.GET, manufacturers)
    context = {"man_filter": man_filter}
    return render(request, "formulary/product_attr.html", context)


def product_detail(request, product_id):
    product = Product_List.objects.get(pk=product_id)
    form = ProductListForm(instance=product, user=request.user)

    if request.method == "POST":
        product = Product_List.objects.get(pk=product_id)
        form = ProductListForm(request.user, request.POST, instance=product)

        if form.is_valid():
            print("Valid")
            form.save()

            return redirect("formulary")

    context = {"product": product, "form": form}
    return render(request, "formulary/product_detail.html", context)


def add_product(request):
    form = ProductListForm(request.user)
    if request.method == "POST":
        form = ProductListForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect("formulary")
        else:
            messages.error(request, "Submitted Form is not Valid")

    context = {"form": form}
    return render(request, "formulary/add_products.html", context)


def add_product_attr(request, item):

    form = form_dict[item]

    if request.method == "POST":
        item_form = form_dict[item]
        form = item_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect("add_product")

    context = {"form": form}
    return render(request, "formulary/add_product_attr.html", context)

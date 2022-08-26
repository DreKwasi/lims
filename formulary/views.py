from unicodedata import category

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse

from .filters import ProductFilter
from .forms import ProductListForm
from .models import *


def formulary_view(request):
    products = Product_List.objects.all()
    product_filter = ProductFilter(request.GET, products)
    context = {
        "product_filter": product_filter,
    }
    return render(request, "formulary/formulary_view.html", context)


def product_detail(request, product_id):
    product = Product_List.objects.get(pk=product_id)
    form = ProductListForm(instance=product, user=request.user)

    if request.method == "POST":
        product = Product_List.objects.get(pk=product_id)
        form = ProductListForm(request.user, request.POST, instance=product)

        if form.is_valid():
            print("Valid")
            form.save()

            return redirect("product_detail", product_id)

    context = {"product": product, "form": form}
    return render(request, "formulary/product_detail.html", context)

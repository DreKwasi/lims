from django.shortcuts import render
from .models import *


def inventory(request):
    stock = Inventory.objects.all()
    context = {"stock": stock}
    return render(request, "inventory/inventory.html", context)


def stock_transfer(request):
    return render(request, "inventory/stock_transfer.html")


def warehouse(request):
    return render(request, "inventory/warehouse.html")


def add_warehouse(request):
    return render(request, "inventory/add_warehouse.html")

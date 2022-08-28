from django.shortcuts import render


def purchase_orders(request):
    return render(request, "inbound/purchase_orders.html")


def add_purchase(request):
    return render(request, "inbound/add_purchase.html")

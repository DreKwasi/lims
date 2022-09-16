from accounts.forms import SupplierForm
from django.forms import modelformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def purchase_orders(request):
    return render(request, "inbound/purchase_orders.html")


def ajax_purchase_order_list_view(request):

    qs = PurchaseOrder.objects.exclude(supplier__isnull=True)
    data = []
    for obj in qs:
        item = {
            "no": obj.id,
            "order number": obj.purchase_order_id,
            "supplier": obj.supplier.supplier_name,
            "date": obj.order_date,
            "amount": obj.total_value,
            "status": obj.order_status,
        }
        data.append(item)
    # import pdb
    # pdb.set_trace()

    return JsonResponse({"data": data})


def add_purchase_order(request):

    Formset = modelformset_factory(
        model=PurchaseOrderProduct,
        form=PurchaseOrderProductForm,
        extra=0,
    )

    formset = Formset()

    supplier_form = SupplierForm()

    if request.method == "GET":
        new_order = PurchaseOrder.objects.create()
        new_order.purchase_order_id = f"PO-{new_order.pk}"
        new_order.save()
        supplier_list = Supplier.objects.all()
        product_list = ProductList.objects.all()
        facility_list = Facility.objects.all()

        po_form = PurchaseOrderForm(instance=new_order)

        context = {
            "supplier_list": supplier_list,
            "po_form": po_form,
            "new_order": new_order,
            "product_list": product_list,
            "facility_list": facility_list,
            "formset": formset,
            "supplier_form": supplier_form,
        }
        return render(request, "inbound/add_purchase_order.html", context)

    elif request.method == "POST":

        objs = request.POST
        new_order = PurchaseOrder.objects.get(
            purchase_order_id=objs["purchase_order_id"]
        )
        po_form = PurchaseOrderForm(request.POST, instance=new_order)
        formset = Formset(data=request.POST)

        if po_form.is_valid() & formset.is_valid():
            po_instance = po_form.save(commit=False)
            po_instance.supplier = Supplier.objects.get(
                supplier_name=objs["supplier"]
            )
            po_instance.facility = Facility.objects.get(
                facility_name=objs["facility"]
            )
            po_instance.save()

            if len(objs.getlist("product")) > 1:
                for form, product in zip(formset, objs.getlist("product")):
                    print(product)
                    pop_instance = form.save(commit=False)
                    pop_instance.product = ProductList.objects.get(
                        product_name=product
                    )
                    pop_instance.purchase_order = po_instance
                    pop_instance.save()
            else:
                pop_instance = formset.save(commit=False)
                pop_instance.product = ProductList.objects.get(
                    product_name=objs["product"]
                )
                pop_instance.purchase_order = po_instance
                pop_instance.save()

        return redirect("purchase_orders")


def get_supplier(request):
    name = request.GET.get("keyword")
    try:
        supplier = Supplier.objects.get(supplier_name=name)
        data = []
        item = {
            "supplier": supplier.supplier_name,
            "address": supplier.address,
            "phone": supplier.phone_number,
            "email": supplier.email,
        }
        data.append(item)
        return JsonResponse({"data": data})

    except Supplier.DoesNotExist:
        return JsonResponse({"data": "Not found"})


def add_supplier_modal(request):
    if request.POST:
        print(request.POST)
        form = SupplierForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return JsonResponse(
                {
                    "data": [
                        {
                            "status": "Done",
                            "message": "New Supplier Has Been Created \n Redirecting...",
                        }
                    ]
                }
            )
        data = []
        for field in form:
            if field.errors.as_text():
                errors = {
                    "status": field.label,
                    "message": field.errors.as_text(),
                }
                data.append(errors)

        return JsonResponse({"data": data})


def detail_purchase_order(request, pk):
    purchase_order = PurchaseOrder.objects.get(id=pk)
    products = purchase_order.purchaseorderproduct_set.all()

    context = {
        "purchase_order": purchase_order,
        "products": products,
    }
    return render(request, "inbound/detail_purchase_order.html", context)

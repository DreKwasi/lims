from collections import defaultdict
from datetime import datetime

from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from formulary.models import ProductList
from inbound.filters import (
    IdentifiedStockFilter,
    PurchaseProductFilter,
    UnloadProductFilter,
)
from inbound.models import (
    IdentifiedStock,
    PurchaseOrder,
    PurchaseOrderProduct,
    Unload,
    UnloadProduct,
)
from inventory.models import LogisticArea

from .serializers import (
    IdentifiedStockSerializer,
    PurchaseOrderSerializer,
    PurchaseProductSerializer,
    UnloadProductSerializer,
    UnloadSerializer,
)


class CreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class UpdateListRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class PurchaseOrderApiViewset(CreateListRetrieveViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        purchase_order = self.get_object()
        serializer = self.serializer_class(purchase_order, data=request.data)

        if serializer.is_valid():

            if len(request.data.getlist("product")) > 1:
                products = request.data.getlist("product")
                open_qty = request.data.getlist("open_quantity")
                planned_qty = request.data.getlist("planned_quantity")
                delivered_qty = request.data.getlist("delivered_quantity")
                prices = request.data.getlist("unit_price")
                discounts = request.data.getlist("discount")

                pending = []
                finished = []

                if request.data["update"] == "":
                    create_objs = []

                    for (
                        product,
                        open_quantity,
                        planned_quantity,
                        delivered_quantity,
                        unit_price,
                        discount,
                    ) in zip(
                        products,
                        open_qty,
                        planned_qty,
                        delivered_qty,
                        prices,
                        discounts,
                    ):
                        formulary_product = ProductList.objects.get(
                            product_name=product
                        )
                        pending.append(
                            True
                            if planned_quantity != open_quantity
                            else False
                        )
                        finished.append(
                            True
                            if delivered_quantity == planned_quantity
                            else False
                        )
                        purchase_product = PurchaseOrderProduct(
                            purchase_order=purchase_order,
                            product=formulary_product,
                            open_quantity=open_quantity,
                            planned_quantity=planned_quantity,
                            delivered_quantity=delivered_quantity,
                            unit_price=unit_price,
                            discount=discount,
                        )
                        create_objs.append(purchase_product)

                    PurchaseOrderProduct.objects.bulk_create(create_objs)

                elif request.data["update"] == "update":
                    purchase_product_ids = request.data.getlist("id")

                    with transaction.atomic():
                        for (
                            purchase_product_id,
                            open_quantity,
                            planned_quantity,
                            delivered_quantity,
                            unit_price,
                            discount,
                        ) in zip(
                            purchase_product_ids,
                            open_qty,
                            planned_qty,
                            delivered_qty,
                            prices,
                            discounts,
                        ):

                            pending.append(
                                True
                                if planned_quantity != open_quantity
                                else False
                            )
                            finished.append(
                                True
                                if delivered_quantity == planned_quantity
                                else False
                            )
                            PurchaseOrderProduct.objects.filter(
                                id=purchase_product_id
                            ).update(
                                open_quantity=int(open_quantity),
                                planned_quantity=int(planned_quantity),
                                delivered_quantity=int(delivered_quantity),
                                unit_price=float(unit_price),
                                discount=float(discount),
                            )

                if all(finished):
                    order_status = "Completed"
                elif any(pending):
                    order_status = "Pending"
                else:
                    order_status = "Ordered"

                serializer.save(order_status=order_status)

            elif len(request.data.getlist("product")) == 1:
                purchase_product = PurchaseProductSerializer(data=request.data)
                purchase_product.is_valid(raise_exception=True)
                instance = purchase_product.validated_data

                print(instance["planned_quantity"], instance["open_quantity"])
                if (
                    instance["delivered_quantity"]
                    == instance["planned_quantity"]
                ):
                    order_status = "Completed"
                elif instance["planned_quantity"] > instance["open_quantity"]:
                    order_status = "Pending"
                else:
                    order_status = "Ordered"

                serializer.save(order_status=order_status)
                purchase_product.update()

            return Response(
                self.serializer_class(purchase_order).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class PurchaseProductApiViewset(CreateListRetrieveViewSet):
    serializer_class = PurchaseProductSerializer
    queryset = PurchaseOrderProduct.objects.all()
    filter_backend = DjangoFilterBackend
    filterset_class = PurchaseProductFilter


class UnloadApiViewset(UpdateListRetrieveViewSet):
    serializer_class = UnloadSerializer
    queryset = Unload.objects.all()

    def update(self, request, pk=None):
        unload = self.get_object()
        serializer = self.serializer_class(unload, data=request.data)

        if serializer.is_valid():
            if len(request.data.getlist("product")) > 1:
                products = request.data.getlist("product")
                open_qtys = request.data.getlist("open_quantity")
                planned_qtys = request.data.getlist("planned_quantity")
                actuals = request.data.getlist("actual_quantity")
                batch_numbers = request.data.getlist("batch_number")
                expiries = request.data.getlist("expiry_date")
                areas = request.data.getlist("area")
                unique_products = set(products)

                indices = defaultdict(list)
                for index, item in enumerate(products):
                    indices[item].append(index)

                statuses = []

                with transaction.atomic():
                    for product in unique_products:

                        batch_actual = [
                            int(actuals[x]) for x in indices[product]
                        ]
                        batch_planned = [
                            int(planned_qtys[x]) for x in indices[product]
                        ]
                        total_planned = sum(batch_planned)
                        total_actual = sum(batch_actual)

                        if total_planned >= total_actual:

                            open_qty = max(
                                [int(open_qtys[x]) for x in indices[product]]
                            )
                            batch_list = [
                                batch_numbers[x] for x in indices[product]
                            ]
                            expiry_list = [
                                expiries[x] for x in indices[product]
                            ]
                            logistic_areas = [
                                LogisticArea.objects.get(area_name=areas[x])
                                for x in indices[product]
                            ]

                            formulary_product = ProductList.objects.get(
                                product_name=product
                            )
                            no_updates = UnloadProduct.objects.filter(
                                unload=unload,
                                product=formulary_product,
                            ).update(
                                open_quantity=open_qty,
                                actual_quantity=total_actual,
                            )
                            unload_product = UnloadProduct.objects.get(
                                unload=unload,
                                product=formulary_product,
                            )

                            objs = []
                            statuses.append(no_updates)

                            if no_updates != 0:
                                for batch, expiry, actual, area in zip(
                                    batch_list,
                                    expiry_list,
                                    batch_actual,
                                    logistic_areas,
                                ):
                                    if batch != "":
                                        objs.append(
                                            IdentifiedStock(
                                                unload_product=unload_product,
                                                batch_number=batch,
                                                expiration_date=datetime.strptime(
                                                    expiry, "%Y-%m-%d"
                                                ),
                                                split_quantity=actual,
                                                target_logistic_area=area,
                                            )
                                        )
                                IdentifiedStock.objects.bulk_create(objs)

                if any(statuses) != 0:
                    serializer.save(status="In Process")
                    return Response(
                        self.serializer_class(unload).data,
                        status.HTTP_201_CREATED,
                    )
                else:
                    return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                product_name = request.data["product"]
                unload_product = UnloadProduct.objects.filter(
                    unload=unload,
                    product=ProductList.objects.get(product_name=product_name),
                )
                unload_product.update(
                    open_quantity=request.data["open_quantity"],
                    actual_quantity=request.data["actual_quantity"],
                )
                IdentifiedStock.objects.create(
                    unload_product=unload_product[0],
                    batch_number=request.data["batch_number"],
                    expiration_date=datetime.strptime(
                        request.data["expiry_date"], "%Y-%m-%d"
                    ),
                    split_quantity=request.data["actual_quantity"],
                    target_logistic_area=request.data["area"],
                )
                serializer.save(status="In Process")
                return Response(
                    self.serializer_class(unload).data,
                    status=status.HTTP_201_CREATED,
                )

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UnloadProductApiViewset(UpdateListRetrieveViewSet):
    serializer_class = UnloadProductSerializer
    queryset = UnloadProduct.objects.all()
    filter_backend = DjangoFilterBackend
    filterset_class = UnloadProductFilter


class IdentifiedStockApiViewset(CreateListRetrieveViewSet):
    serializer_class = IdentifiedStockSerializer
    queryset = IdentifiedStock.objects.all()
    filter_backend = DjangoFilterBackend
    filterset_class = IdentifiedStockFilter

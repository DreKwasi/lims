from django.db import models


class PriceList(models.Model):
    product = models.ForeignKey(
        "formulary.productlist",
        on_delete=models.CASCADE,
    )
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

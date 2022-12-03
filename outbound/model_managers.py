from django.db import models
from utils.queryset import CustomQuerySet


class StockTransferManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

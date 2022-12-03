from django.db import models

from utils.queryset import CustomQuerySet


class PurchaseOrderManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class PurchaseOrderProductManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class UnloadManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

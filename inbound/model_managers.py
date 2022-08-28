from django.db import models
from .queryset import CustomQuerySet


class UnloadManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class PutAwayManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

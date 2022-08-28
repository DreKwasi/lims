from django.db import models
from django.dispatch import Signal


post_update = Signal()


class CustomQuerySet(models.query.QuerySet):
    def update(self, *args, **kwargs):
        super(CustomQuerySet, self).update(kwargs)
        post_update.send(sender=self.model)

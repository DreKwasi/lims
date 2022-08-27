from django.contrib import admin
from .models import *


admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderProduct)
admin.site.register(Unload)
admin.site.register(Put_Away)

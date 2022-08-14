from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = (
        "category_name",
        "slug",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Generic_Attr)
admin.site.register(Form)
admin.site.register(Tier)
admin.site.register(Product_List)

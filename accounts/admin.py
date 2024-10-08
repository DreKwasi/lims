from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = ("email", "first_name", "username")
    readonly_fields = (
        "last_login",
        "date_joined",
    )
    ordering = (
        "-date_joined",
        "first_name",
    )
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)


class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        "facility_name",
        "contact_person",
        "phone_number",
        "is_active",
    )
    readonly_fields = ("created_date",)
    ordering = ("-created_date",)


admin.site.register(Facility, FacilityAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "supplier_name",
        "contact_person",
        "phone_number",
        "is_active",
    )
    readonly_fields = ("created_date",)
    ordering = ("-created_date",)


admin.site.register(Supplier, SupplierAdmin)

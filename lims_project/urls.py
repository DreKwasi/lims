from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("formulary/api/", include("formulary.api.urls")),
    path("formulary/", include("formulary.urls")),
    path("inventory/api/", include("inventory.api.urls")),
    path("inventory/", include("inventory.urls")),
    path("accounts/api/", include("accounts.api.urls")),
    path("acounts/", include("accounts.urls")),
    path("inbound/api/", include("inbound.api.urls")),
    path("inbound/", include("inbound.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path(
        "",
        TemplateView.as_view(template_name="base.html"),
        name="home",
    )
]

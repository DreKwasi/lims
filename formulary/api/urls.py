from django.urls import path

from .views import *

urlpatterns = [
    path("product-list", ProductListApiView.as_view()),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hydro_app.views import HydroponicSystemViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r"systems", HydroponicSystemViewSet)
router.register(r"measurements", MeasurementViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

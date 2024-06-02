from django.urls import path
from .views import HydroponicSystemCreate, HydroponicSystemMeasurementCreate

urlpatterns = [
    path(
        "create-system/",
        HydroponicSystemCreate.as_view(),
        name="system-create",
    ),
    path(
        "create-measurement/",
        HydroponicSystemMeasurementCreate.as_view(),
        name="measurement-create",
    ),
]

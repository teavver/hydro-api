from django.urls import path
from .views import (
    HydroponicSystemListCreateView,
    HydroponicSystemRetrieveUpdateDeleteView,
    HydroponicSystemLatestMeasurementsView,
    HydroponicSystemMeasurementListCreateView,
)

urlpatterns = [
    path(
        "",
        HydroponicSystemListCreateView.as_view(),
        name="system-list-create",
    ),
    path(
        "<int:pk>/",
        HydroponicSystemRetrieveUpdateDeleteView.as_view(),
        name="system-detail",
    ),
    path(
        "<int:pk>/latest-measurements/",
        HydroponicSystemLatestMeasurementsView.as_view(),
        name="system-latest-measurements",
    ),
    path(
        "measurements/",
        HydroponicSystemMeasurementListCreateView.as_view(),
        name="measurement-list-create",
    ),
]

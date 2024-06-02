from django_filters import rest_framework as filters
from .models import HydroponicSystemMeasurement


class HydroponicSystemMeasurementFilter(filters.FilterSet):
    """
    When retrieving measurements from a system, allow the User to filter by:
    - Temperature range (min-max)
    - Date range (start-end)
    The date (created_at property) is set when the measurement is created
    """

    min_temperature = filters.NumberFilter(field_name="temperature", lookup_expr="gte")
    max_temperature = filters.NumberFilter(field_name="temperature", lookup_expr="lte")
    start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = HydroponicSystemMeasurement
        fields = ["min_temperature", "max_temperature", "start_date", "end_date"]

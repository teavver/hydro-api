from rest_framework import generics, permissions
from django_filters import rest_framework, filters
from .models import HydroponicSystem, HydroponicSystemMeasurement
from .filters import HydroponicSystemMeasurementFilter
from .serializers import (
    HydroponicSystemSerializer,
    HydroponicSystemMeasurementSerializer,
)


# Systems
class HydroponicSystemListCreateView(generics.ListCreateAPIView):
    """
    Endpoint to list and create new Systems
    """

    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HydroponicSystemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint to retrieve, update, and delete hydroponic systems
    """

    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)


# Measurements
class HydroponicSystemMeasurementListCreateView(generics.ListCreateAPIView):
    """
    Endpoint to list and create measurements for existing Systems
    Supports filtering and sorting.
    """

    serializer_class = HydroponicSystemMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = HydroponicSystemMeasurementFilter
    # Allow filtering by date, temperature, pH and TDS
    ordering_fields = ["created_at", "temperature", "pH", "TDS"]

    def get_queryset(self):
        return HydroponicSystemMeasurement.objects.filter(
            system__owner=self.request.user
        )

    def perform_create(self, serializer):
        hydroponic_system_id = self.request.data.get("system")
        hydroponic_system = HydroponicSystem.objects.get(
            id=hydroponic_system_id, owner=self.request.user
        )
        serializer.save(system=hydroponic_system)


class HydroponicSystemLatestMeasurementsView(generics.ListAPIView):
    """
    API endpoint to return the 10 latest measurements for a specific System.
    """

    serializer_class = HydroponicSystemMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        system_id = self.kwargs["pk"]
        return HydroponicSystemMeasurement.objects.filter(
            system__id=system_id, system__owner=self.request.user
        ).order_by("-created_at")[:10]
